import http
import json
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Union

from flask import Flask, jsonify, make_response, request
from flask.wrappers import Response
from flask_cors import CORS, cross_origin

import service_layer.lti.config.ToolConfigJson as ToolConfigJson
import utils.logger as logger
from errors import errors as err
from repositories import orm
from service_layer import services, unit_of_work
from utils import constants as cons
from utils.constants import (
    role_admin_string,
    role_course_creator_string,
    role_student_string,
    role_teacher_string,
)
from utils.decorators import debug_only, json_only

from entrypoints.endpoints.lms import bp_lms
from entrypoints.endpoints.user import bp_user
from entrypoints.endpoints.course import bp_course

app = Flask(__name__)
CORS(app, supports_credentials=True)
orm.start_mappers()

app.register_blueprint(bp_lms)
app.register_blueprint(bp_user)
app.register_blueprint(bp_course)

logger.configure_dict()

mocked_frontend_log = {
    "logs": [
        {
            "name": "FID",
            "value": 1.900000000372529,
            "rating": "good",
            "delta": 1.900000000372529,
            "entries": [
                {
                    "name": "pointerdown",
                    "entryType": "first-input",
                    "startTime": 1611.5,
                    "duration": 8,
                    "processingStart": 1613.4000000003725,
                    "processingEnd": 1613.4000000003725,
                    "cancelable": True,
                }
            ],
            "id": "v3-1665130071366-6352791670096",
            "navigationType": "reload",
        }
    ]
}


@app.errorhandler(Exception)
def handle_general_exception(ex):
    response = json.dumps({"error": ex.__class__.__name__, "message": str(ex)})
    logger.error(response)
    return response, 500


@app.errorhandler(err.AException)
def handle_custom_exception(ex: err.AException):
    response = json.dumps({"error": ex.__class__.__name__, "message": ex.message})
    logger.error(response)
    return response, ex.status_code


# ##### LTI ENDPOINTS #####
# 1. LTI login is the first step of the
# OIDC Login workflow initiated by the platform
@app.route("/lti_login", methods=["POST"])
@cross_origin(supports_credentials=True)
def lti_login():
    return services.get_oidc_login(request)


# 2. After the platform has verified the LTI launch request,
# it uses this endpoint to which we redirected
@app.route("/lti_launch", methods=["POST"])
@cross_origin(supports_credentials=True)
def lti_launch():
    return services.get_lti_launch(request)


# 3. Get cookie for frontend if end of OIDC Login workflow
# by using a short living valid nonce
@app.route("/login", methods=["POST"])
@cross_origin(supports_credentials=True)
def login():
    return services.get_login(request)


# 4. Logout by deleting cookie
@app.route("/logout", methods=["GET"])
@cross_origin(supports_credentials=True)
def logout():
    return services.get_logout(request)


# Send the enpoint which launches the LTI tool to the frontend
@app.route("/lti_launch_view", methods=["GET"])
@cross_origin(supports_credentials=True)
def lti_launch_view():
    return {
        "lti_launch_view": ToolConfigJson.get_haski_activity_url(
            os.environ.get("LMS_URL", "https://moodle.haski.app")
        )
    }, 200


# Test Endpoint to post a user login by id and get a user by id
@app.route("/login_credentials", methods=["POST"])
@cross_origin(supports_credentials=True)
@debug_only
@json_only()
def login_credentials(data: Dict[str, Any]):
    method = request.method
    match method:
        case "POST":
            condition1 = data is not None
            condition2 = "lms_user_id" in data
            if condition1 and condition2:
                condition3 = type(data["lms_user_id"]) is int
                if condition3:
                    user = services.get_student_by_user_id(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        data["lms_user_id"],
                    )
                    status_code = 201
                    return jsonify(user), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


# unused
# Post to add a learning path algorithm
@app.route("/algorithm", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def post_learning_path_algorithm(data: Dict[str, Any]):
    match request.method:
        case "POST":
            condition1 = data is not None
            condition2 = "short_name" in data and "full_name" in data
            if condition1 and condition2:
                condition3 = (
                    type(data["short_name"]) is str and type(data["full_name"]) is str
                )
                available_algorithms = ["graf", "aco", "ga", "default"]
                condition4 = data["short_name"].lower() in available_algorithms
                if condition3 and condition4:
                    result = services.create_learning_path_algorithm(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        data["short_name"].lower(),
                        data["full_name"],
                    )
                    return jsonify(result), 201
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


# unused
# Post to add a topic visit for a student
@app.route("/lms/student/<student_id>/<lms_user_id>/topic/<topic_id>", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def post_student_topic_visit(data: Dict[str, Any], student_id, lms_user_id, topic_id):
    method = request.method
    match method:
        case "POST":
            condition1 = data is not None
            condition2 = "visit_start" in data
            if condition1 and condition2:
                condition3 = re.search(cons.date_format_search, data["visit_start"])
                condition4 = type(data["visit_start"]) is str
                if condition3 and condition4:
                    visit_start = datetime.strptime(
                        data["visit_start"], cons.date_format
                    ).date()
                    result = services.add_student_topic_visit(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student_id,
                        topic_id,
                        visit_start,
                        (
                            data["previous_topic_id"]
                            if "previous_topic_id" in data
                            else None
                        ),
                    )
                    status_code = 201
                    return jsonify(result), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


# unused
# Post to add a learning element visit for a student
@app.route(
    "/lms/student/<student_id>/<lms_user_id>/learningElement/"
    + "<learning_element_id>",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
@json_only()
def post_student_learning_element_id_visit(
    data: Dict[str, Any], student_id, lms_user_id, learning_element_id
):
    method = request.method
    match method:
        case "POST":
            condition1 = data is not None
            condition2 = "visit_start" in data
            if condition1 and condition2:
                condition3 = type(data["visit_start"]) is str
                condition4 = re.search(cons.date_format_search, data["visit_start"])
                if condition3 and condition4:
                    visit_start = datetime.strptime(
                        data["visit_start"], cons.date_format
                    ).date()
                    result = services.add_student_learning_element_visit(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student_id,
                        learning_element_id,
                        visit_start,
                    )
                    status_code = 201
                    return jsonify(result), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


# unused
@app.route(
    "/student/<student_id>/topic/<topic_id>/algorithm",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
@json_only()
def post_student_learning_path_learning_element_algorithm(
    data: Dict[str, Any], student_id: int, topic_id: int
):
    match request.method:
        case "POST":
            condition1 = data is not None
            condition2 = "algorithm" in data
            if condition1 and condition2:
                condition3 = type(data["algorithm"]) is str
                available_algorithms = ["graf", "aco", "ga", "default"]
                condition4 = data["algorithm"].lower() in available_algorithms
                if condition3 and condition4:
                    algorithm = data["algorithm"].lower()
                    algorithm_id = services.get_learning_path_algorithm_by_short_name(
                        unit_of_work.SqlAlchemyUnitOfWork(), algorithm
                    )["id"]
                    r = services.add_student_lpath_le_algorithm(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student_id,
                        topic_id,
                        algorithm_id,
                    )
                    return jsonify(r), 201
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


# unused
@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course" + "/<course_id>",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_course_by_course_id(user_id, lms_user_id, student_id, course_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_course_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id, course_id
            )
            status_code = 200
            return jsonify(result), status_code


# unused
@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course"
    + "/<course_id>/topic/<topic_id>",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_topics_by_student_course_and_topic_id(
    user_id, lms_user_id, student_id, course_id, topic_id
):
    method = request.method
    match method:
        case "GET":
            result = services.get_topic_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                course_id,
                student_id,
                topic_id,
            )
            status_code = 200
            return jsonify(result), status_code


# unused
@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course"
    + "/<course_id>/topic/<topic_id>/learningElement",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_element_by_student_course_and_topic_id(
    user_id, lms_user_id, student_id, course_id, topic_id
):
    method = request.method
    match method:
        case "GET":
            result = services.get_learning_elements_for_course_and_topic_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id,
            )
            status_code = 200
            return jsonify(result), status_code


# unused
@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course"
    + "/<course_id>/topic/<topic_id>/learningElement/"
    + "<learning_element_id>",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_element_by_le_id(
    user_id, lms_user_id, student_id, course_id, topic_id, learning_element_id
):
    method = request.method
    match method:
        case "GET":
            result = services.get_learning_element_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id,
                learning_element_id,
            )
            status_code = 200
            return jsonify(result), status_code


# Learning Path Endpoints
# unused
@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course/"
    + "<course_id>/topic/<topic_id>/learningPath",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
@json_only()
def learning_path_administration(
    data: Dict[str, Any], user_id, lms_user_id, student_id, course_id, topic_id
):
    method = request.method
    match method:
        case "POST":
            condition1 = data is not None
            condition2 = "algorithm" in data
            if condition1 and condition2:
                available_algorithms = ["graf", "aco", "ga", "default"]
                condition3 = type(data["algorithm"]) is str
                condition4 = data["algorithm"].lower() in available_algorithms
                if condition3 and condition4:
                    result = services.create_learning_path(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        user_id,
                        lms_user_id,
                        student_id,
                        course_id,
                        topic_id,
                        data["algorithm"].lower(),
                    )
                    status_code = 201
                    return jsonify(result), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


# specific roles can trigger calculation of learningpaths for all students for a topic
# calculation on basis of student-algorithm (if empty teacher algorithm)
# useful when: creating a new topic
@app.route(
    "/v2/user/<user_id>/course/<course_id>/topic/<topic_id>/learningPath",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
@json_only()
def post_calculate_learning_path_for_all_students(
    data: Dict[str, Any], user_id: str, course_id: str, topic_id: str
):
    match request.method:
        case "POST":
            condition2 = "university" in data
            condition4 = "role" in data
            if not (condition2 and condition4):
                raise err.MissingParameterError()

            condition6 = type(data["university"]) is str
            condition8 = type(data["role"]) is str
            if not (condition6 and condition8):
                raise err.WrongParameterValueError()

            available_roles = [
                role_admin_string,
                role_course_creator_string,
                role_teacher_string,
            ]
            condition9 = data["role"].lower() in available_roles
            if not condition9:
                raise err.NoValidRoleError()

            # Get unit of work.
            uow = unit_of_work.SqlAlchemyUnitOfWork()

            # Get student and their courses.
            students = services.get_all_students(unit_of_work.SqlAlchemyUnitOfWork())

            results = []
            for student in students:
                student_user_id = services.get_user_by_id(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    student["user_id"],
                    None,
                )

                topic = services.get_topic_by_id(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    None,
                    None,
                    course_id,
                    None,
                    topic_id,
                )

                if topic["contains_le"]:
                    # Get algorithm for the topic.
                    algorithm = services.get_student_lpath_le_algorithm(
                        uow, student["id"], topic["id"]
                    ) or services.get_lpath_le_algorithm_by_topic(uow, topic["id"])

                    lpath_algorithm = services.get_learning_path_algorithm_by_id(
                        uow, algorithm["algorithm_id"]
                    )

                    # Create learning path.
                    results.append(
                        services.create_learning_path(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            student_user_id["id"],
                            student_user_id["lms_user_id"],
                            student["id"],
                            course_id,
                            topic["id"],
                            lpath_algorithm["short_name"].lower(),
                        )
                    )

            # Return results with status code.
            status_code = 201
            return jsonify(results), status_code


# User Endpoints
# unused
@app.route("/user/<user_id>/<lms_user_id>", methods=["GET"])
@cross_origin(supports_credentials=True)
def user_by_user_id(user_id, lms_user_id):
    method = request.method
    match method:
        case "GET":
            user = services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id
            )
            status_code = 200
            return jsonify(user), status_code


# Get algorithm set by teacher for a topic
@app.route("/topic/<topic_id>/teacherAlgorithm", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_teacher_lp_le_algorithm(topic_id: str):
    method = request.method
    match method:
        case "GET":
            algorithm = services.get_lpath_le_algorithm_by_topic(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )
            algorithm["short_name"] = services.get_learning_path_algorithm_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), algorithm["algorithm_id"]
            )["short_name"]
            status_code = 200
            return jsonify(algorithm), status_code


# unused
# Get settings by user id
@app.route("/user/<user_id>/<lms_user_id>/settings", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_settings_by_user_id(user_id, lms_user_id):
    method = request.method
    match method:
        case "GET":
            settings = services.get_settings_for_user(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id
            )
            status_code = 200
            return jsonify(settings), status_code


# unused
# Delete contact form by user id
@app.route("/user/<user_id>/<lms_user_id>/contactform", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_contact_form(user_id, lms_user_id):
    services.delete_contact_form(unit_of_work.SqlAlchemyUnitOfWork(), user_id)
    return "ok", 201


# unused
# Post to add news
@app.route("/news", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def news_creation(data: Dict[str, Any]):
    for el in ["language_id", "news_content", "expiration_date"]:
        if el not in data:
            raise err.MissingParameterError()

    result = services.create_news(
        unit_of_work.SqlAlchemyUnitOfWork(),
        data["university"],
        data["language_id"],
        datetime.today().date(),
        data["news_content"],
        datetime.strptime(data["expiration_date"], cons.date_format).date(),
    )

    if result is None:
        raise err.NewsError()

    status_code = 201
    return jsonify(result), status_code


# Get news by language and university
@app.route("/news/language/<language_id>/university/<university>", methods=["GET"])
@app.route(
    "/news/language/<language_id>/university/",
    defaults={"university": None},
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def news(language_id, university):
    result = services.get_news(
        unit_of_work.SqlAlchemyUnitOfWork(),
        language_id,
        university,
        datetime.today().date(),
    )
    status_code = 200
    return jsonify(result), status_code


# unused
# Delete all news
@app.route("/news", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_news():
    services.delete_news(unit_of_work.SqlAlchemyUnitOfWork())
    return "ok", 201


# Post Logbuffer for a user
@app.route("/user/<user_id>/logbuffer", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def create_logbuffer(content, user_id):
    # raises exception if user does not exsist
    services.get_user_by_id(unit_of_work.SqlAlchemyUnitOfWork(), user_id, None)

    if not content:
        raise err.MissingParameterError()

    result = services.create_logbuffer(
        unit_of_work.SqlAlchemyUnitOfWork(),
        user_id,
        content,
        datetime.today(),
    )

    if result is None:
        raise err.LogBufferError()

    return make_response(jsonify(result), http.HTTPStatus.CREATED)


# unused
# Get Logbuffer for a user
@app.route("/user/<user_id>/logbuffer", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_logbuffer_by_user_id(user_id):
    result = services.get_logbuffer(unit_of_work.SqlAlchemyUnitOfWork(), user_id)
    return make_response(jsonify(result), http.HTTPStatus.OK)


# unused
# Delete Logbuffer for a user
@app.route("/user/<user_id>/logbuffer", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_logbuffer_by_user_id(user_id):
    services.delete_logbuffer(unit_of_work.SqlAlchemyUnitOfWork(), user_id)
    return Response(status=http.HTTPStatus.NO_CONTENT)


# Log Endpoints
@app.route("/logs/frontend", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def logging_frontend(data: Dict[str, Any]):
    method = request.method
    required_log_attributes = [
        "name",
        "value",
        "rating",
        "delta",
        "entries",
        "id",
        "navigationType",
    ]
    available_names = ["FCP", "TTFB", "CLS", "LCP", "FID", "INP"]
    available_ratings = ["good", "needs-improvement", "poor"]
    available_navigation_type = [
        "navigate",
        "reload",
        "back-forward",
        "back-forward-cache",
        "prerender",
    ]
    missing_value = False
    match method:
        case "POST":
            for key in required_log_attributes:
                if data is None or key not in data:
                    missing_value = True
            if missing_value:
                raise err.MissingParameterError()
            con1 = data["name"] in available_names
            con2 = data["rating"] in available_ratings
            con3 = data["navigationType"] in available_navigation_type
            if not con1 and con2 and con3:
                raise err.WrongParameterValueError()
            mocked_frontend_log["logs"].append(data)
            status_code = 201
            return jsonify(data), status_code


# unused
# Post to add a student rating
@app.route("/student/<student_id>/topic/<topic_id>/rating", methods=["POST"])
@cross_origin(supports_credentials=True)
def post_create_student_rating(student_id: str, topic_id: str):
    match request.method:
        case "POST":
            result = services.create_student_rating(
                uow=unit_of_work.SqlAlchemyUnitOfWork(),
                student_id=int(student_id),
                topic_id=int(topic_id),
                timestamp=datetime.now(),
            )
            status_code = 201
            return jsonify(result), status_code


# Get all the studentratings
@app.route("/user/<user_id>/student/<student_id>/rating", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_student_ratings(user_id: str, student_id: str):
    match request.method:
        case "GET":
            student = services.get_student_by_user_id(
                uow=unit_of_work.SqlAlchemyUnitOfWork(), user_id=user_id
            )
            if student["id"] == int(student_id):
                result = services.get_student_ratings(
                    uow=unit_of_work.SqlAlchemyUnitOfWork()
                )
                status_code = 200
                return jsonify(result), status_code
            else:
                raise err.WrongParameterValueError()


# unused
# Post to add a learning element rating
@app.route(
    "/topic/<topic_id>/learningElement/<learning_element_id>/rating", methods=["POST"]
)
@cross_origin(supports_credentials=True)
def post_create_learning_element_rating(topic_id: str, learning_element_id: str):
    match request.method:
        case "POST":
            result = services.create_learning_element_rating(
                uow=unit_of_work.SqlAlchemyUnitOfWork(),
                topic_id=int(topic_id),
                learning_element_id=int(learning_element_id),
                timestamp=datetime.now(),
            )
            status_code = 201
            return jsonify(result), status_code


# Get all the learning element ratings
@app.route("/learningElement/rating", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_learning_element_ratings():
    match request.method:
        case "GET":
            result = services.get_learning_element_ratings(
                uow=unit_of_work.SqlAlchemyUnitOfWork()
            )
            status_code = 200
            return jsonify(result), status_code


if __name__ == "__main__":
    app.run(port=5000, debug=True)

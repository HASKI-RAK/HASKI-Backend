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

#unused
@app.route("/lms/course/<course_id>/student/<student_id>", methods=["POST"])
@cross_origin(supports_credentials=True)
def post_student_course(course_id, student_id):
    method = request.method
    match method:
        case "POST":
            student_course = services.add_student_to_course(
                unit_of_work.SqlAlchemyUnitOfWork(), student_id, course_id
            )
            if student_course != {}:
                return make_response(jsonify(student_course), http.HTTPStatus.CREATED)
            else:
                return make_response(
                    jsonify({"CREATED": False}), http.HTTPStatus.CONFLICT
                )

#unused
@app.route("/lms/course/<course_id>/teacher/<teacher_id>", methods=["POST"])
@cross_origin(supports_credentials=True)
def post_teacher_course(course_id, teacher_id):
    method = request.method
    match method:
        case "POST":
            teacher_course = services.add_teacher_to_course(
                unit_of_work.SqlAlchemyUnitOfWork(), teacher_id, course_id
            )
            status_code = 201
            return jsonify(teacher_course), status_code

#unused
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

#unused
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

#unused
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

#unused
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

#unused
@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course"
    + "/<course_id>/topic/<topic_id>/subtopic",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_sub_topics_by_topic_id(user_id, lms_user_id, student_id, course_id, topic_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_sub_topic_by_topic_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id,
            )
            status_code = 200
            return jsonify(result), status_code

#unused
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

#unused
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
#unused
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


@app.route(
    "/user/<user_id>/course/"
    + "<course_id>/topic/<topic_id>/learningElement/<learning_element_lms_id>/rating",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
def post_calculate_rating(
    user_id: str, course_id: str, topic_id: str, learning_element_lms_id: str
):
    match request.method:
        case "POST":
            # uow
            uow = unit_of_work.SqlAlchemyUnitOfWork()

            # Get user by user id.
            user = services.get_user_by_id(uow=uow, user_id=user_id, lms_user_id=None)

            # Get student by user id.
            student = services.get_student_by_user_id(uow=uow, user_id=user_id)

            # Get learning element by learning element id.
            learning_element_by_lms = services.get_learning_element_by_lms_id(
                uow=uow,
                student_id=student["id"],
                learning_element_lms_id=learning_element_lms_id,
            )

            learning_element = services.get_learning_element_by_id(
                uow=uow,
                user_id=user_id,
                lms_user_id=user["lms_user_id"],
                student_id=student["id"],
                course_id=course_id,
                topic_id=topic_id,
                learning_element_id=learning_element_by_lms["id"],
            )

            # Init result and status code.
            result = {}
            status_code = 201

            # Get the activity type.
            activity_type = learning_element["activity_type"]
            available_activity_types = ["h5pactivity"]

            # Early return if the activity type is not supported.
            if activity_type not in available_activity_types:
                return jsonify(result), status_code

            # Get classification of learning element id.
            classification = learning_element["classification"]
            available_classifications = ["ÜB", "SE"]

            # Early return if the classification is not available.
            if classification not in available_classifications:
                return jsonify(result), status_code

            # Get the attempt from moodle.
            response = services.get_moodle_most_recent_attempt_by_user(
                uow=uow,
                course_id=int(course_id),
                learning_element_id=int(learning_element_lms_id),
                lms_user_id=str(user["lms_user_id"]),
            )

            # Update the ratings.
            if response != {}:
                result = services.update_ratings(
                    uow=uow,
                    student_id=student["id"],
                    learning_element_id=int(learning_element["id"]),
                    topic_id=int(topic_id),
                    attempt_result=response.get("success", 0),
                    timestamp=datetime.fromtimestamp(response["timecreated"]),
                )

            # Return result with status code.
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course/"
    + "<course_id>/topic/<topic_id>/learningPath",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_path(user_id, lms_user_id, student_id, course_id, topic_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_learning_path(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
                topic_id,
            )
            status_code = 200
            return jsonify(result), status_code


# get default learning path for all students in a university
@app.route(
    "/user/<user_id>/<lms_user_id>/defaultLearningPath",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_default_learning_path(user_id, lms_user_id):
    method = request.method
    match method:
        case "GET":
            user = services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id
            )
            result = services.get_default_learning_path_by_university(
                unit_of_work.SqlAlchemyUnitOfWork(), user["university"]
            )
            return make_response(jsonify(result), http.HTTPStatus.OK)


# Create/Overwrite default learning path for all students in a university
@app.route(
    "/user/<user_id>/<lms_user_id>/defaultLearningPath",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
@json_only()
def create_default_learning_path(
    data: List[Dict[str, Union[str, int, bool]]], user_id, lms_user_id
):
    method = request.method
    match method:
        case "POST":
            condition1 = bool(data) and all(
                (
                    "classification" in item
                    and "position" in item
                    and "disabled" in item
                    and "university" in item
                )
                for item in data
            )
            if not condition1:
                return make_response(http.HTTPStatus.BAD_REQUEST)

            user = services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id
            )
            permitted_roles = [
                role_admin_string,
                role_course_creator_string,
                role_teacher_string,
            ]
            condition2 = user["role"] in permitted_roles

            if condition2:
                condition3 = services.get_default_learning_path_by_university(
                    unit_of_work.SqlAlchemyUnitOfWork(), user["university"]
                )
                if condition3:
                    services.delete_default_learning_path_by_uni(
                        unit_of_work.SqlAlchemyUnitOfWork(), user["university"]
                    )
                results = []
                for item in data:
                    results.append(
                        services.create_default_learning_path_element(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            item["classification"],
                            item["position"],
                            item["disabled"],
                            user["university"],
                        )
                    )
                # Recalculate "Default" learningpaths for all students
                courses = services.get_courses_by_uni(
                    unit_of_work.SqlAlchemyUnitOfWork(), user["university"]
                )
                students = services.get_all_students(
                    unit_of_work.SqlAlchemyUnitOfWork()
                )
                for student in students:
                    student_user_id = services.get_user_by_id(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student["user_id"],
                        None,
                    )
                    for course in courses["courses"]:
                        topics = services.get_topics_for_course_id(
                            unit_of_work.SqlAlchemyUnitOfWork(), course["id"]
                        )
                        for topic in topics:
                            current_topic = services.get_topic_by_id(
                                unit_of_work.SqlAlchemyUnitOfWork(),
                                None,
                                None,
                                course["id"],
                                None,
                                topic["id"],
                            )
                            results_learning_pahts = []
                            if current_topic["contains_le"]:
                                results_learning_pahts.append(
                                    services.create_learning_path(
                                        unit_of_work.SqlAlchemyUnitOfWork(),
                                        student_user_id["id"],
                                        student_user_id["lms_user_id"],
                                        student["id"],
                                        course["id"],
                                        topic["id"],
                                        "default",
                                    )
                                )
                return make_response(jsonify(results), http.HTTPStatus.CREATED)


# User Endpoints
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


@app.route("/user/<user_id>/<lms_user_id>/settings", methods=["PUT", "DELETE"])
@cross_origin(supports_credentials=True)
@json_only(ignore=["DELETE"])
def settings_by_user_id_administration(data: Dict[str, Any], user_id, lms_user_id):
    method = request.method
    match method:
        case "PUT":
            condition1 = "theme" in data
            condition2 = "pswd" in data
            if condition1:
                settings = services.update_settings_for_user(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    user_id,
                    data["theme"],
                    data["pswd"] if condition2 else None,
                )
                status_code = 201
                return jsonify(settings), status_code
            else:
                raise err.MissingParameterError()
        case "DELETE":
            settings = services.reset_settings(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id
            )
            result = settings
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/topic/<topic_id>/studentAlgorithm", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_student_lp_le_algorithm(user_id: str, topic_id: str):
    method = request.method
    match method:
        case "GET":
            student_id = services.get_student_by_user_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id
            )["id"]
            algorithm = services.get_student_lpath_le_algorithm(
                unit_of_work.SqlAlchemyUnitOfWork(), student_id, topic_id
            )
            algorithm["short_name"] = services.get_learning_path_algorithm_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), algorithm["algorithm_id"]
            )["short_name"]
            status_code = 200
            return jsonify(algorithm), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/course/<course_id>"
    + "/topic/<topic_id>/studentAlgorithm",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
@json_only(ignore=["GET"])
def post_student_lp_le_algorithm(
    data: Dict[str, Any], user_id: str, lms_user_id: int, course_id: int, topic_id: int
):
    method = request.method
    match method:
        case "POST":
            condition1 = "algorithm_short_name" in data
            if condition1:
                condition2 = type(data["algorithm_short_name"]) is str
                algorithm = services.get_learning_path_algorithm_by_short_name(
                    unit_of_work.SqlAlchemyUnitOfWork(), data["algorithm_short_name"]
                )
                condition3 = algorithm != {}
                if condition2 and condition3:
                    student_id = services.get_student_by_user_id(
                        unit_of_work.SqlAlchemyUnitOfWork(), user_id
                    )["id"]
                    student_lpath_le_algorithm = (
                        services.get_student_lpath_le_algorithm(
                            unit_of_work.SqlAlchemyUnitOfWork(), student_id, topic_id
                        )
                    )
                    if student_lpath_le_algorithm == {}:
                        result = services.add_student_lpath_le_algorithm(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            student_id,
                            topic_id,
                            algorithm["id"],
                        )
                        status_code = 201
                        return jsonify(result), status_code
                    else:
                        result = services.update_student_lpath_le_algorithm(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            student_id,
                            topic_id,
                            algorithm["id"],
                        )
                        services.create_learning_path(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            user_id,
                            lms_user_id,
                            student_id,
                            course_id,
                            topic_id,
                            data["algorithm_short_name"].lower(),
                        )
                        status_code = 201

                        return jsonify(result), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


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


@app.route(
    "/user/<user_id>/<lms_user_id>/topic/<topic_id>/teacherAlgorithm", methods=["POST"]
)
@cross_origin(supports_credentials=True)
@json_only(ignore=["GET"])
def post_teacher_lp_le_algorithm(
    data: Dict[str, Any], user_id: str, lms_user_id: str, topic_id: str
):
    method = request.method
    match method:
        case "POST":
            condition1 = "algorithm_short_name" in data
            if not condition1:
                raise err.MissingParameterError()

            user = services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id
            )
            permitted_roles = [
                role_admin_string,
                role_course_creator_string,
                role_teacher_string,
            ]
            condition2 = user["role"] in permitted_roles
            if not condition2:
                raise err.UnauthorizedError()

            condition3 = type(data["algorithm_short_name"]) is str
            algorithm = services.get_learning_path_algorithm_by_short_name(
                unit_of_work.SqlAlchemyUnitOfWork(), data["algorithm_short_name"]
            )
            condition4 = algorithm != {}
            if not (condition3 and condition4):
                raise err.WrongParameterValueError()

            result = {}
            lp_le_algorithm = services.get_lpath_le_algorithm_by_topic(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )
            if lp_le_algorithm == {}:
                # here all available students should get their
                # student_learning_path_learning_element_algorithm
                # on behalf of the set teacher_algorithm
                students = services.get_all_students(
                    unit_of_work.SqlAlchemyUnitOfWork()
                )
                for student in students:
                    student_id = student["id"]
                    services.add_student_lpath_le_algorithm(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student_id,
                        topic_id,
                        algorithm["id"],
                    )
                result = services.create_learning_path_learning_element_algorithm(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    topic_id,
                    algorithm["id"],
                )
            else:
                result = services.update_learning_path_learning_element_algorithm(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    topic_id,
                    data["algorithm_short_name"],
                )

            status_code = 201
            return jsonify(result), status_code


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


@app.route("/user/<user_id>/<lms_user_id>/contactform", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def contact_form(data: Dict[str, Any], user_id, lms_user_id):
    for el in ["report_type", "report_topic", "report_description"]:
        if el not in data:
            raise err.MissingParameterError()

    result = services.create_contact_form(
        unit_of_work.SqlAlchemyUnitOfWork(),
        user_id,
        lms_user_id,
        data["report_type"],
        data["report_topic"],
        data["report_description"],
        datetime.today(),
    )

    if result is None:
        raise err.ContactFormError()

    status_code = 201
    return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/contactform", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_contact_form(user_id, lms_user_id):
    services.delete_contact_form(unit_of_work.SqlAlchemyUnitOfWork(), user_id)
    return "ok", 201


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


@app.route("/news", methods=["DELETE"])
@cross_origin(supports_credentials=True)
def delete_news():
    services.delete_news(unit_of_work.SqlAlchemyUnitOfWork())
    return "ok", 201


# Logbuffer
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


@app.route("/user/<user_id>/logbuffer", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_logbuffer_by_user_id(user_id):
    result = services.get_logbuffer(unit_of_work.SqlAlchemyUnitOfWork(), user_id)
    return make_response(jsonify(result), http.HTTPStatus.OK)


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


# Admin Endpoints
@app.route("/user/<user_id>/<lms_user_id>/admin/<admin_id>/user", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_users_by_admin(user_id, lms_user_id, admin_id):
    method = request.method
    match method:
        case "GET":
            users = services.get_users_by_admin(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id
            )
            status_code = 200
            return jsonify(users), status_code


@app.route("/user/<user_id>/<lms_user_id>/admin/<admin_id>/logs", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_admin_logs(user_id, lms_user_id, admin_id):
    method = request.method
    match method:
        case "GET":
            services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id
            )
            return_message = mocked_frontend_log
            status_code = 200
            return jsonify(return_message), status_code


# Teacher Endpoints
@app.route("/user/<user_id>/<lms_user_id>/teacher/<teacher_id>/course", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_teacher_courses(user_id, lms_user_id, teacher_id):
    method = request.method
    match method:
        case "GET":
            courses = services.get_courses_for_teacher(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, teacher_id
            )
            status_code = 200
            return jsonify(courses), status_code


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


@app.route(
    "/user/<user_id>/course/<course_id>/topic/<topic_id>/recommendation",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_element_recommendation(user_id: str, course_id: str, topic_id: str):
    # uow
    uow = unit_of_work.SqlAlchemyUnitOfWork()

    # Get user by user id.
    user = services.get_user_by_id(uow=uow, user_id=user_id, lms_user_id=None)

    # Get student by user id.
    student = services.get_student_by_user_id(uow=uow, user_id=user_id)

    # Get all recommended exercises for student in topic.
    results = services.get_recommended_exercises_for_student_in_topic(
        uow=uow,
        user_id=user_id,
        lms_user_id=user["lms_user_id"],
        student_id=student["id"],
        topic_id=topic_id,
        course_id=course_id,
    )

    status_code = 200
    return jsonify(results), status_code


if __name__ == "__main__":
    app.run(port=5000, debug=True)

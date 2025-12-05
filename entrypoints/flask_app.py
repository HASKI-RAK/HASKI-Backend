import http
import json
import os
import re
from datetime import datetime
from typing import Any, Dict, List, Union

from flask import Flask, jsonify, make_response, request
from flask.wrappers import Response
from flask_cors import CORS, cross_origin

import service_layer.crypto.JWTKeyManagement as JWTKeyManagement
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

app = Flask(__name__)
CORS(app, supports_credentials=True)
orm.start_mappers()

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
    response = json.dumps(
        {"error": ex.__class__.__name__, "message": ex.message})
    logger.error(response)
    return response, ex.status_code


# User Administration via LMS
@app.route("/lms/user", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def create_user(data: Dict[str, Any]):
    method = request.method
    match method:
        case "POST":
            condition1 = "name" in data
            condition2 = "university" in data
            condition3 = "lms_user_id" in data
            condition4 = "role" in data
            if condition1 and condition2 and condition3 and condition4:
                condition5 = type(data["name"]) is str
                condition6 = type(data["university"]) is str
                condition7 = type(data["lms_user_id"]) is int
                condition8 = type(data["role"]) is str
                if condition5 and condition6 and condition7 and condition8:
                    role = data["role"].lower()
                    available_roles = [
                        role_admin_string,
                        role_course_creator_string,
                        role_student_string,
                        role_teacher_string,
                    ]
                    if role not in available_roles:
                        raise err.NoValidRoleError()
                    else:
                        user = services.create_user(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            data["name"],
                            data["university"],
                            data["lms_user_id"],
                            role,
                        )
                        status_code = 201
                        return jsonify(user), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()


@app.route("/lms/user/<user_id>/<lms_user_id>", methods=["PUT", "DELETE"])
@cross_origin(supports_credentials=True)
@json_only(ignore=["DELETE"])
def user_administration(data, user_id, lms_user_id):
    method = request.method
    match method:
        case "PUT":
            condition1 = "name" in data
            condition2 = "university" in data
            if condition1 and condition2:
                condition3 = type(data["name"]) is str
                condition4 = type(data["university"]) is str
                if condition3 and condition4:
                    user = services.update_user(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        int(user_id),
                        int(lms_user_id),
                        data["name"],
                        data["university"],
                    )
                    status_code = 201
                    return jsonify(user), status_code
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()
        case "DELETE":
            services.delete_user(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id
            )
            result = {"message": cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_user_by_id(user_id, lms_user_id):
    method = request.method
    match method:
        case "GET":
            user = services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id
            )
            status_code = 200
            return jsonify(user), status_code


# Add all students that are enrolled in moodle courses to the haski courses
@app.route("/course/<course_id>/allStudents", methods=["POST"])
@cross_origin(supports_credentials=True)
def add_all_students_to_course(course_id):
    method = request.method
    match method:
        case "POST":
            created_for = []
            students = services.get_all_students(
                unit_of_work.SqlAlchemyUnitOfWork())
            for student in students:
                user = services.get_user_by_id(
                    unit_of_work.SqlAlchemyUnitOfWork(
                    ), student["user_id"], None
                )
                courses = services.get_enrolled_university_courses(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    user["lms_user_id"],
                    user["university"],
                )
                if services.is_student_enrolled_in_course(courses, course_id):
                    services.add_student_to_course(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        student["id"],
                        course_id,
                    )
                    created_for.append(student["id"])
            if created_for:
                return make_response(
                    jsonify(
                        {
                            "CREATED": True,
                            "course_id": course_id,
                            "student_count": len(created_for),
                        }
                    ),
                    http.HTTPStatus.CREATED,
                )

            return make_response(
                jsonify(
                    {"CREATED": False, "course_id": course_id, "student_count": 0}),
                http.HTTPStatus.NOT_FOUND,
            )


# Add a course
# noinspection PyPackageRequirements
@app.route("/lms/course", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def post_course(data: Dict[str, Any]):
    method = request.method
    match method:
        case "POST":
            condition1 = data is not None
            condition2 = "name" in data
            condition3 = "lms_id" in data
            condition4 = "university" in data
            condition5 = "created_by" in data
            if not (
                condition1 and condition2 and condition3 and condition4 and condition5
            ):
                raise err.MissingParameterError()

            condition6 = type(data["lms_id"]) is int
            condition7 = type(data["name"]) is str
            condition8 = type(data["university"]) is str
            condition9 = type(data["created_by"]) is int
            if not (condition6 and condition7 and condition8 and condition9):
                raise err.WrongParameterValueError(
                    message=cons.date_format_message)

            current_date = datetime.now().strftime(cons.date_format)
            start_date = datetime.strptime(current_date, cons.date_format)

            condition10 = (
                "start_date" in data
                and isinstance(data["start_date"], str)
                and re.search(cons.date_format_search, data["start_date"]) is not None
            )
            if condition10:
                start_date = datetime.strptime(
                    data["start_date"], cons.date_format)

            created_at = datetime.strptime(current_date, cons.date_format)
            course = services.create_course(
                unit_of_work.SqlAlchemyUnitOfWork(),
                data["lms_id"],
                data["name"],
                data["university"],
                data["created_by"],
                created_at,
                start_date,
            )

            status_code = 201
            return jsonify(course), status_code


@app.route("/lms/course/<course_id>/<lms_course_id>", methods=["PUT", "DELETE"])
@cross_origin(supports_credentials=True)
@json_only(ignore=["DELETE"])
def course_administration(data: Dict[str, Any], course_id, lms_course_id):
    method = request.method
    match method:
        case "PUT":
            condition1 = data is not None
            condition2 = "name" in data
            condition3 = "university" in data
            condition4 = "last_updated" in data
            if not (condition1 and condition2 and condition3 and condition4):
                raise err.MissingParameterError()

            condition5 = re.search(
                cons.date_format_search, data["last_updated"])
            if not condition5:
                raise err.WrongParameterValueError()

            start_date = None
            condition6 = "start_date" in data
            if condition6:
                condition7 = re.search(
                    cons.date_format_search, data["start_date"])
                if not condition7:
                    raise err.WrongParameterValueError()

                start_date = datetime.strptime(
                    data["start_date"], cons.date_format
                ).date()

            course = services.update_course(
                unit_of_work.SqlAlchemyUnitOfWork(),
                course_id,
                lms_course_id,
                data["name"],
                data["university"],
                start_date,
            )

            status_code = 201
            return jsonify(course), status_code
        case "DELETE":
            topics = services.get_topics_for_course_id(
                unit_of_work.SqlAlchemyUnitOfWork(), course_id
            )
            services.delete_learning_paths_by_course_id(
                unit_of_work.SqlAlchemyUnitOfWork(), course_id
            )
            for topic in topics:
                services.delete_student_topic_by_topic_id(
                    unit_of_work.SqlAlchemyUnitOfWork(), topic["id"]
                )
                services.delete_learning_path_learning_element_algorithm(
                    unit_of_work.SqlAlchemyUnitOfWork(), topic["id"]
                )
                services.delete_student_lpath_le_algorithm(
                    unit_of_work.SqlAlchemyUnitOfWork(), topic["id"]
                )
                services.delete_student_ratings_by_topic(
                    unit_of_work.SqlAlchemyUnitOfWork(), topic["id"]
                )
                services.delete_learning_element_ratings_by_topic(
                    unit_of_work.SqlAlchemyUnitOfWork(), topic["id"]
                )

                learning_elements = services.get_learning_elements_for_topic_id(
                    unit_of_work.SqlAlchemyUnitOfWork(), topic["id"]
                )

                for learning_element in learning_elements:
                    services.delete_student_learning_element_by_learning_element_id(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        learning_element["learning_element_id"],
                    )
                    services.delete_learning_element(
                        unit_of_work.SqlAlchemyUnitOfWork(),
                        learning_element["learning_element_id"],
                    )

                services.delete_topic(
                    unit_of_work.SqlAlchemyUnitOfWork(), topic["id"])

            services.delete_course(
                unit_of_work.SqlAlchemyUnitOfWork(), course_id)
            result = {"message": cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code


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


# Get user info from cookie
@app.route("/lms/user_from_cookie", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_user_info():
    method = request.method
    state_jwt = request.cookies.get("haski_state")
    if state_jwt is None:
        raise err.StateNotMatchingError()

    if not JWTKeyManagement.verify_jwt_payload(
        JWTKeyManagement.verify_jwt(state_jwt), verify_nonce=False
    ):
        raise err.UnauthorizedError()
    state = JWTKeyManagement.verify_jwt(state_jwt)
    match method:
        case "GET":
            user = services.get_student_by_user_id(
                unit_of_work.SqlAlchemyUnitOfWork(), state["user_id"]
            )
            status_code = 200
            return jsonify(user), status_code


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


# Endpoint to get activity status for a student for a course
@app.route(
    "/lms/course/<course_id>/student/<lms_user_id>/activitystatus", methods=["GET"]
)
@cross_origin(supports_credentials=True)
def get_activity_status_for_student(course_id, lms_user_id):
    method = request.method
    match method:
        case "GET":
            activity_status = services.get_activity_status_for_student_for_course(
                unit_of_work.SqlAlchemyUnitOfWork(), course_id, lms_user_id
            )
            return jsonify(activity_status), 200


# Endpoint to get activity status for a student, course and specific learning element
@app.route(
    "/lms/course/<course_id>/student/<student_id>/"
    + "learningElementId/<learning_element_id>/activitystatus",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_activity_status_for_student_for_learning_element(
    course_id, student_id, learning_element_id
):
    method = request.method
    match method:
        case "GET":
            activity_status = services.get_activity_status_for_learning_element(
                unit_of_work.SqlAlchemyUnitOfWork(),
                course_id,
                student_id,
                learning_element_id,
            )
            return jsonify(activity_status), 200


@app.route(
    "/lms/user/<user_id>/remote/courses",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_all_remote_courses(user_id):
    method = request.method
    match method:
        case "GET":
            user = services.get_user_by_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, None
            )
            enrolled_moodle_courses = services.get_courses_for_user_from_moodle(
                unit_of_work.SqlAlchemyUnitOfWork(), user["lms_user_id"]
            )

            return jsonify(enrolled_moodle_courses), 200


@app.route(
    "/lms/remote/course/<course_id>/content",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_remote_topics_and_learning_elements_from_course(course_id):
    method = request.method
    match method:
        case "GET":
            remote_courses = services.get_topics_and_elements_from_moodle_course(
                unit_of_work.SqlAlchemyUnitOfWork(), course_id
            )
            return jsonify(remote_courses), 200


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
                    type(data["short_name"]) is str and type(
                        data["full_name"]) is str
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


@app.route("/lms/course/<course_id>/topic", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def post_topic(data: Dict[str, Any], course_id):
    method = request.method
    match method:
        case "POST":
            condition1 = data is not None
            condition2 = "name" in data
            condition3 = "lms_id" in data
            condition4 = "is_topic" in data
            condition5 = "contains_le" in data
            condition6 = "created_by" in data
            condition7 = "created_at" in data
            condition8 = "university" in data
            if not (
                condition1
                and condition2
                and condition3
                and condition4
                and condition5
                and condition6
                and condition7
                and condition8
            ):
                raise err.MissingParameterError()

            condition9 = type(data["name"]) is str
            condition10 = type(data["lms_id"]) is int
            condition11 = type(data["is_topic"]) is bool
            condition12 = type(data["contains_le"]) is bool
            condition13 = type(data["created_by"]) is str
            condition14 = type(data["created_at"]) is str
            condition15 = type(data["university"]) is str
            if not (
                condition9
                and condition10
                and condition11
                and condition12
                and condition13
                and condition14
                and condition15
            ):
                raise err.WrongParameterValueError()

            condition16 = re.search(
                cons.date_format_search, data["created_at"])
            if not condition16:
                raise err.WrongParameterValueError(
                    message=cons.date_format_message)

            created_at = datetime.strptime(
                data["created_at"], cons.date_format).date()

            topic = services.create_topic(
                unit_of_work.SqlAlchemyUnitOfWork(),
                course_id,
                data["lms_id"],
                data["is_topic"],
                data["parent_id"] if "parent_id" in data else None,
                data["contains_le"],
                data["name"],
                data["university"],
                data["created_by"],
                created_at,
            )

            status_code = 201
            return jsonify(topic), status_code


# Add Topic to course and add all students to it
@app.route("/course/<course_id>/topics/allStudents", methods=["POST"])
@cross_origin(supports_credentials=True)
def add_all_students_to_all_topics(course_id):
    method = request.method
    match method:
        case "POST":
            uow = unit_of_work.SqlAlchemyUnitOfWork()
            students = services.get_all_students(uow)
            created_for = []

            for student in students:
                user = services.get_user_by_id(uow, student["user_id"], None)

                # look if student is enrolled in the course
                courses = services.get_courses_by_student_id(
                    uow, user["id"], user["lms_user_id"], student["id"]
                )

                if services.is_student_enrolled_in_course(courses, course_id):
                    services.add_student_to_topics(
                        uow, student["id"], course_id)
                    created_for.append(student["id"])

            if created_for:
                return make_response(
                    jsonify(
                        {
                            "CREATED": True,
                            "course_id": course_id,
                            "student_count": len(created_for),
                        }
                    ),
                    http.HTTPStatus.CREATED,
                )

            return make_response(
                jsonify(
                    {"CREATED": False, "course_id": course_id, "student_count": 0}),
                http.HTTPStatus.NOT_FOUND,
            )


@app.route(
    "/lms/topic/<topic_id>/<lms_topic_id>",
    methods=["PUT", "DELETE"],
)
@cross_origin(supports_credentials=True)
@json_only(ignore=["DELETE"])
def topic_administration(data: Dict[str, Any], topic_id, lms_topic_id):
    method = request.method
    match method:
        case "PUT":
            condition1 = data is not None
            condition2 = "name" in data
            condition3 = "is_topic" in data
            condition4 = "contains_le" in data
            condition5 = "created_by" in data
            condition6 = "created_at" in data
            condition7 = "university" in data
            condition8 = "last_updated" in data
            if not (
                condition1
                and condition2
                and condition3
                and condition4
                and condition5
                and condition6
                and condition7
                and condition8
            ):
                raise err.MissingParameterError()

            condition9 = re.search(
                cons.date_format_search, data["last_updated"])
            condition10 = re.search(
                cons.date_format_search, data["created_at"])
            if not (condition9 and condition10):
                raise err.NoValidParameterValueError()

            created_at = datetime.strptime(
                data["created_at"], cons.date_format).date()

            last_updated = datetime.strptime(
                data["last_updated"], cons.date_format
            ).date()

            topic = services.update_topic(
                unit_of_work.SqlAlchemyUnitOfWork(),
                topic_id,
                lms_topic_id,
                data["is_topic"],
                data["parent_id"],
                data["contains_le"],
                data["name"],
                data["university"],
                data["created_by"],
                created_at,
                last_updated,
            )

            status_code = 201
            return jsonify(topic), status_code
        case "DELETE":
            services.delete_learning_paths_by_topic_id(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )
            services.delete_student_topic_by_topic_id(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )
            services.delete_learning_path_learning_element_algorithm(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )
            services.delete_student_lpath_le_algorithm(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )
            services.delete_student_ratings_by_topic(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )
            services.delete_learning_element_ratings_by_topic(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )

            learning_elements = services.get_learning_elements_for_topic_id(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id
            )

            for learning_element in learning_elements:
                services.delete_student_learning_element_by_learning_element_id(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    learning_element["learning_element_id"],
                )
                services.delete_learning_element(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    learning_element["learning_element_id"],
                )

            services.delete_topic(
                unit_of_work.SqlAlchemyUnitOfWork(), topic_id)
            result = {"message": cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code


# Create LE - shorter request-url
@app.route(
    "/lms/topic/<topic_id>/learningElement",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
@json_only()
def create_learning_element(data: Dict[str, Any], topic_id):
    method = request.method
    match method:
        case "POST":
            condition1 = data is not None
            condition2 = "lms_id" in data
            condition3 = "activity_type" in data
            condition4 = "classification" in data
            condition5 = "name" in data
            condition6 = "created_by" in data
            condition7 = "created_at" in data
            condition8 = "university" in data
            if not (
                condition1
                and condition2
                and condition3
                and condition4
                and condition5
                and condition6
                and condition7
                and condition8
            ):
                raise err.MissingParameterError()

            condition9 = isinstance(data["lms_id"], int)
            condition10 = isinstance(data["activity_type"], str)
            condition11 = isinstance(data["classification"], str)
            condition12 = isinstance(data["name"], str)
            condition13 = isinstance(data["created_by"], str)
            condition14 = isinstance(data["created_at"], str)
            condition15 = isinstance(data["university"], str)
            if not (
                condition9
                and condition10
                and condition11
                and condition12
                and condition13
                and condition14
                and condition15
            ):
                raise err.WrongParameterValueError()

            condition16 = re.search(
                cons.date_format_search, data["created_at"])
            if not condition16:
                raise err.WrongParameterValueError(
                    message=cons.date_format_message)

            created_at = datetime.strptime(
                data["created_at"], cons.date_format).date()

            learning_element = services.create_learning_element(
                unit_of_work.SqlAlchemyUnitOfWork(),
                topic_id,
                data["lms_id"],
                data["activity_type"],
                data["classification"],
                data["name"],
                data["created_by"],
                created_at,
                data["university"],
            )

            students = services.get_all_students(
                unit_of_work.SqlAlchemyUnitOfWork())

            for student in students:
                student_id = student["id"]
                services.add_student_to_learning_element(
                    unit_of_work.SqlAlchemyUnitOfWork(),
                    learning_element["id"],
                    student_id,
                )

            status_code = 201
            return jsonify(learning_element), status_code


@app.route(
    "/lms/learningElement/<learning_element_id>/<lms_learning_element_id>",
    methods=["PUT", "DELETE"],
)
@cross_origin(supports_credentials=True)
@json_only(ignore=["DELETE"])
def learning_element_administration(
    data: Dict[str, Any],
    learning_element_id,
    lms_learning_element_id,
):
    method = request.method
    match method:
        case "PUT":
            condition1 = data is not None
            condition2 = "activity_type" in data
            condition3 = "classification" in data
            condition4 = "name" in data
            condition5 = "created_by" in data
            condition6 = "created_at" in data
            condition7 = "university" in data
            condition8 = "last_updated" in data
            if not (
                condition1
                and condition2
                and condition3
                and condition4
                and condition5
                and condition6
                and condition7
                and condition8
            ):
                raise err.MissingParameterError()

            condition10 = isinstance(data["activity_type"], str)
            condition11 = isinstance(data["classification"], str)
            condition12 = isinstance(data["name"], str)
            condition13 = isinstance(data["created_by"], str)
            condition14 = isinstance(data["created_at"], str)
            condition15 = isinstance(data["university"], str)
            condition16 = isinstance(data["last_updated"], str)
            if not (
                condition10
                and condition11
                and condition12
                and condition13
                and condition14
                and condition15
                and condition16
            ):
                raise err.WrongParameterValueError()

            condition17 = re.search(
                cons.date_format_search, data["created_at"])
            condition18 = re.search(
                cons.date_format_search, data["last_updated"])
            if not (condition17 and condition18):
                raise err.WrongParameterValueError(
                    message=cons.date_format_message)

            created_at = datetime.strptime(
                data["created_at"], cons.date_format).date()

            last_updated = datetime.strptime(
                data["last_updated"], cons.date_format
            ).date()

            learning_element = services.update_learning_element(
                unit_of_work.SqlAlchemyUnitOfWork(),
                learning_element_id,
                lms_learning_element_id,
                data["activity_type"],
                data["classification"],
                data["name"],
                data["created_by"],
                created_at,
                last_updated,
                data["university"],
            )

            status_code = 201
            return jsonify(learning_element), status_code
        case "DELETE":
            services.delete_learning_path_learning_element_by_le_id(
                unit_of_work.SqlAlchemyUnitOfWork(), learning_element_id
            )
            services.delete_student_learning_element_by_learning_element_id(
                unit_of_work.SqlAlchemyUnitOfWork(), learning_element_id
            )
            services.delete_learning_element_ratings_by_learning_element(
                unit_of_work.SqlAlchemyUnitOfWork(), learning_element_id
            )
            services.delete_learning_element(
                unit_of_work.SqlAlchemyUnitOfWork(), learning_element_id
            )
            result = {"message": cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code


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
                condition3 = re.search(
                    cons.date_format_search, data["visit_start"])
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
                condition4 = re.search(
                    cons.date_format_search, data["visit_start"])
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


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course/"
    + "<course_id>/learningElement",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_elements_for_course(user_id, lms_user_id, student_id, course_id):
    method = request.method
    match method:
        case "GET":
            learning_elements = services.get_learning_elements_for_course_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
            )
            status_code = 200
            return jsonify(learning_elements), status_code


# Student Endpoints
@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "learningCharacteristics",
    methods=["DELETE"],
)
@cross_origin(supports_credentials=True)
def delete_learning_characteristics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "DELETE":
            characteristic = services.reset_learning_characteristics(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id, student_id
            )
            status_code = 200
            return jsonify(characteristic), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>" + "/learningCharacteristics",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_characteristics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "GET":
            characteristic = services.get_learning_characteristics(
                unit_of_work.SqlAlchemyUnitOfWork(), student_id, user_id, lms_user_id
            )
            status_code = 200
            return jsonify(characteristic), status_code


@app.route("/lms/student/<student_id>/questionnaire/ils", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def questionnaire_ils(data: Dict[str, Any], student_id):
    method = request.method
    match method:
        case "POST":
            condition = "ils" in data
            if not condition:
                raise err.MissingParameterError()

            ils = {}
            for key in data["ils"]:
                ils[key["question_id"]] = key["answer"]

            required_answers_ils = [
                "vv_2_f7",
                "vv_5_f19",
                "vv_7_f27",
                "vv_10_f39",
                "vv_11_f43",
                "si_1_f2",
                "si_4_f14",
                "si_7_f26",
                "si_10_f38",
                "si_11_f42",
                "ar_3_f9",
                "ar_4_f13",
                "ar_6_f21",
                "ar_7_f25",
                "ar_8_f29",
                "sg_1_f4",
                "sg_2_f8",
                "sg_4_f16",
                "sg_10_f40",
                "sg_11_f44",
            ]

            for key in required_answers_ils:
                if key not in ils.keys():
                    raise err.MissingParameterError()

            for answer in ils.values():
                if not isinstance(answer, str):
                    raise err.WrongParameterValueError()
                if answer != "a" and answer != "b":
                    raise err.NoValidParameterValueError()

            result = services.create_questionnaire_ils(
                uow=unit_of_work.SqlAlchemyUnitOfWork(),
                student_id=student_id,
                ils_answers=ils,
            )

            status_code = 201
            return jsonify(result), status_code


@app.route("/lms/student/<student_id>/questionnaire/listk", methods=["POST"])
@cross_origin(supports_credentials=True)
@json_only()
def questionnaire_list_k(data: Dict[str, Any], student_id):
    method = request.method
    match method:
        case "POST":
            condition = "list_k" in data
            if not condition:
                raise err.MissingParameterError()

            list_k = {}
            for key in data["list_k"]:
                list_k[key["question_id"]] = key["answer"]

            required_answers_list_k = [
                "org1_f1",
                "org2_f2",
                "org3_f3",
                "elab1_f4",
                "elab2_f5",
                "elab3_f6",
                "crit_rev1_f7",
                "crit_rev2_f8",
                "crit_rev3_f9",
                "rep1_f10",
                "rep2_f11",
                "rep3_f12",
                "goal_plan1_f13",
                "goal_plan2_f14",
                "goal_plan3_f15",
                "con1_f16",
                "con2_f17",
                "con3_f18",
                "reg1_f19",
                "reg2_f20",
                "reg3_f21",
                "att1_f22",
                "att2_f23",
                "att3_f24",
                "eff1_f25",
                "eff2_f26",
                "eff3_f27",
                "time1_f28",
                "time2_f29",
                "time3_f30",
                "lrn_w_cls1_f31",
                "lrn_w_cls2_f32",
                "lrn_w_cls3_f33",
                "lit_res1_f34",
                "lit_res2_f35",
                "lit_res3_f36",
                "lrn_env1_f37",
                "lrn_env2_f38",
                "lrn_env3_f39",
            ]

            for key in required_answers_list_k:
                if key not in list_k.keys():
                    raise err.MissingParameterError()

            for answer in list_k.values():
                if not isinstance(answer, int):
                    raise err.WrongParameterValueError()
                if answer > 5 or answer < 0:
                    raise err.NoValidParameterValueError()

            result = services.create_questionnaire_list_k(
                uow=unit_of_work.SqlAlchemyUnitOfWork(),
                student_id=student_id,
                list_k_answers=list_k,
            )

            status_code = 201
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "learningStyle",
    methods=["PUT", "DELETE"],
)
@cross_origin(supports_credentials=True)
@json_only(ignore=["DELETE"])
def learning_style_administration(
    data: Dict[str, Any], user_id, lms_user_id, student_id
):
    method = request.method
    match method:
        case "PUT":
            condition1 = data is not None
            condition2 = "perception_dimension" in data
            condition3 = "perception_value" in data
            condition4 = "input_dimension" in data
            condition5 = "input_value" in data
            condition6 = "processing_dimension" in data
            condition7 = "processing_value" in data
            condition8 = "understanding_dimension" in data
            condition9 = "understanding_value" in data
            if (
                condition1
                and condition2
                and condition3
                and condition4
                and condition5
                and condition6
                and condition7
                and condition8
                and condition9
            ):
                condition10 = type(data["perception_dimension"]) is str
                condition11 = type(data["perception_value"]) is int
                condition12 = type(data["input_dimension"]) is str
                condition13 = type(data["input_value"]) is int
                condition14 = type(data["processing_dimension"]) is str
                condition15 = type(data["processing_value"]) is int
                condition16 = type(data["understanding_dimension"]) is str
                condition17 = type(data["understanding_value"]) is int
                if (
                    condition10
                    and condition11
                    and condition12
                    and condition13
                    and condition14
                    and condition15
                    and condition16
                    and condition17
                ):
                    condition18 = 0 < data["perception_value"] < 12
                    condition19 = 0 < data["input_value"] < 12
                    condition20 = 0 < data["processing_value"] < 12
                    condition21 = 0 < data["understanding_value"] < 12
                    if condition18 and condition19 and condition20 and condition21:
                        result = services.update_learning_style_by_student_id(
                            unit_of_work.SqlAlchemyUnitOfWork(),
                            user_id,
                            lms_user_id,
                            student_id,
                            data["perception_dimension"],
                            data["perception_value"],
                            data["input_dimension"],
                            data["input_value"],
                            data["processing_dimension"],
                            data["processing_value"],
                            data["understanding_dimension"],
                            data["understanding_value"],
                        )
                        status_code = 201
                        return jsonify(result), status_code
                    else:
                        raise err.WrongLearningStyleDimensionError()
                else:
                    raise err.WrongParameterValueError()
            else:
                raise err.MissingParameterError()
        case "DELETE":
            result = services.reset_learning_style_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id, student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "learningStyle",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_style(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_learning_style_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "learningStrategy",
    methods=["DELETE"],
)
@cross_origin(supports_credentials=True)
def delete_learning_strategy(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "DELETE":
            result = services.reset_learning_strategy_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id, student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "learningStrategy",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_strategy(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_learning_strategy_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "learningAnalytics",
    methods=["DELETE"],
)
@cross_origin(supports_credentials=True)
def delete_learning_analytics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "DELETE":
            result = services.reset_learning_analytics_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id, student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "learningAnalytics",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_learning_analytics(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_learning_analytics_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "knowledge",
    methods=["DELETE"],
)
@cross_origin(supports_credentials=True)
def delete_knowledge(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "DELETE":
            result = services.reset_knowledge_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id, student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/" + "knowledge", methods=["GET"]
)
@cross_origin(supports_credentials=True)
def get_knowledge(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_knowledge_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), student_id
            )
            status_code = 200
            return jsonify(result), status_code


@app.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course", methods=["GET"])
@cross_origin(supports_credentials=True)
def get_courses_by_student_id(user_id, lms_user_id, student_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_courses_by_student_id(
                unit_of_work.SqlAlchemyUnitOfWork(), user_id, lms_user_id, student_id
            )
            status_code = 200
            return jsonify(result), status_code


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


@app.route(
    "/user/<user_id>/<lms_user_id>/student/<student_id>/course/<course_id>/topic",
    methods=["GET"],
)
@cross_origin(supports_credentials=True)
def get_topics_by_student_and_course_id(user_id, lms_user_id, student_id, course_id):
    method = request.method
    match method:
        case "GET":
            result = services.get_topics_by_student_and_course_id(
                unit_of_work.SqlAlchemyUnitOfWork(),
                user_id,
                lms_user_id,
                student_id,
                course_id,
            )
            status_code = 200
            return jsonify(result), status_code


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


@app.route(
    "/user/<user_id>/<lms_user_id>/learningPath",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
@json_only()
def post_calculate_learning_path(_: Dict[str, Any], user_id: str, lms_user_id: str):
    match request.method:
        case "POST":
            # Get unit of work.
            uow = unit_of_work.SqlAlchemyUnitOfWork()

            # Get student and their courses.
            student = services.get_student_by_user_id(uow, user_id)
            courses = services.get_courses_by_student_id(
                uow, user_id, lms_user_id, student["id"]
            )

            # If there are no courses, initiate an empty array
            results = []

            for course in courses["courses"]:
                # Get every available topic in all course.
                topics = list(
                    services.get_topics_by_student_and_course_id(
                        uow, user_id, lms_user_id, student["id"], course["id"]
                    )["topics"]
                )
                for topic in topics:
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
                                user_id,
                                lms_user_id,
                                student["id"],
                                course["id"],
                                topic["id"],
                                lpath_algorithm["short_name"].lower(),
                            )
                        )
            # Return results with status code.
            status_code = 201
            return jsonify(results), status_code


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
            students = services.get_all_students(
                unit_of_work.SqlAlchemyUnitOfWork())

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
            user = services.get_user_by_id(
                uow=uow, user_id=user_id, lms_user_id=None)

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
            result = services.recalculate_learning_path(
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
                    unit_of_work.SqlAlchemyUnitOfWork(
                    ), data["algorithm_short_name"]
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
                unit_of_work.SqlAlchemyUnitOfWork(
                ), data["algorithm_short_name"]
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
    result = services.get_logbuffer(
        unit_of_work.SqlAlchemyUnitOfWork(), user_id)
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

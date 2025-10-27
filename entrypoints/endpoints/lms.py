from flask import Blueprint
from flask_cors import cross_origin
from flask import request, jsonify
from utils.decorators import json_only
from typing import Dict, Any
from service_layer import services, unit_of_work
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement
from errors import errors as err
from utils import constants as cons
import re
from datetime import datetime
from utils.constants import (
    role_admin_string,
    role_course_creator_string,
    role_student_string,
    role_teacher_string,
)
bp_lms = Blueprint('lms', __name__)


# User Administration via LMS
@bp_lms.route("/lms/user", methods=["POST"])
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


@bp_lms.route("/lms/user/<user_id>/<lms_user_id>", methods=["PUT", "DELETE"])
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
        
# Get user info from cookie
@bp_lms.route("/lms/user_from_cookie", methods=["GET"])
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

@bp_lms.route(
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

# Add a course
# noinspection PyPackageRequirements
@bp_lms.route("/lms/course", methods=["POST"])
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
                raise err.WrongParameterValueError(message=cons.date_format_message)

            current_date = datetime.now().strftime(cons.date_format)
            start_date = datetime.strptime(current_date, cons.date_format)

            condition10 = (
                "start_date" in data
                and isinstance(data["start_date"], str)
                and re.search(cons.date_format_search, data["start_date"]) is not None
            )
            if condition10:
                start_date = datetime.strptime(data["start_date"], cons.date_format)

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


@bp_lms.route("/lms/course/<course_id>/<lms_course_id>", methods=["PUT", "DELETE"])
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

            condition5 = re.search(cons.date_format_search, data["last_updated"])
            if not condition5:
                raise err.WrongParameterValueError()

            start_date = None
            condition6 = "start_date" in data
            if condition6:
                condition7 = re.search(cons.date_format_search, data["start_date"])
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

                services.delete_topic(unit_of_work.SqlAlchemyUnitOfWork(), topic["id"])

            services.delete_course(unit_of_work.SqlAlchemyUnitOfWork(), course_id)
            result = {"message": cons.deletion_message}
            status_code = 200
            return jsonify(result), status_code


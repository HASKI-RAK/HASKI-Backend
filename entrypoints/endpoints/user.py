from flask import Blueprint, make_response
from flask_cors import cross_origin
from flask import request, jsonify
from service_layer import services, unit_of_work
from utils.decorators import json_only
from errors import errors as err
from typing import Dict, Any, List, Union
from datetime import datetime
import http
from utils.constants import (
    role_admin_string,
    role_course_creator_string,
    role_teacher_string,
)
bp_user = Blueprint('user', __name__)

#get learning elements for a course by user_id
@bp_user.route(
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

# get user by id
@bp_user.route("/user/<user_id>/<lms_user_id>", methods=["GET"])
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


# Update or Delete settings for user / delete is unused
@bp_user.route("/user/<user_id>/<lms_user_id>/settings", methods=["PUT", "DELETE"])
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

# Post to a contact form
@bp_user.route("/user/<user_id>/<lms_user_id>/contactform", methods=["POST"])
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


# Post to change the learning path algorithm set by teacher for a topic
@bp_user.route(
    "/user/<user_id>/<lms_user_id>/topic/<topic_id>/teacherAlgorithm", methods=["POST"]
)
@cross_origin(supports_credentials=True)
def post_teacher_lp_le_algorithm(
   user_id: str, lms_user_id: str, topic_id: str
):
    data = request.get_json()
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

# Post to calculate learning path for a user
@bp_user.route(
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

# get courses by student id
@bp_user.route("/user/<user_id>/<lms_user_id>/student/<student_id>/course", methods=["GET"])
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
        
# get topics by student id and course id
@bp_user.route(
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

# Get learning path for a student
@bp_user.route(
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

# Create/Overwrite default learning path for all students in a university
@bp_user.route(
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


# get default learning path for all students in a university
@bp_user.route(
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

# Post to change the learning path algorithm for a student for a topic
@bp_user.route(
    "/user/<user_id>/<lms_user_id>/course/<course_id>"
    + "/topic/<topic_id>/studentAlgorithm",
    methods=["POST"],
)
@cross_origin(supports_credentials=True)
def post_student_lp_le_algorithm(
    user_id: str, lms_user_id: int, course_id: int, topic_id: int
):
    data = request.get_json()
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


# get the algorithm selected by the student for a topic
@bp_user.route("/user/<user_id>/topic/<topic_id>/studentAlgorithm", methods=["GET"])
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


# Post to calculate rating for a learning element for a user
@bp_user.route(
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

#get learning characteristics of a student
@bp_user.route(
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

#delete learning characteristics of a student
@bp_user.route(
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

#update or delete learning style of a student
@bp_user.route(
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

#get learning style of a student
@bp_user.route(
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

#get learning strategy of a student
@bp_user.route(
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

#delete learning strategy of a student
@bp_user.route(
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
        
#get learning analytics of a student
@bp_user.route(
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

#delete learning analytics of a student
@bp_user.route(
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
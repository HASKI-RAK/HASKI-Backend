from flask import Blueprint
from flask_cors import cross_origin
from flask import request, jsonify
from service_layer import services, unit_of_work
from utils.decorators import json_only
from errors import errors as err
from typing import Dict, Any
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

#get user by id
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

#get knowledge of a student
@bp_user.route(
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
            return jsonify(result), 

#delete knowledge of a student
@bp_user.route(
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
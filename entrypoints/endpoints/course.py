from flask import Blueprint, make_response
from flask_cors import cross_origin
from flask import request, jsonify
from service_layer import services, unit_of_work

import http

bp_course = Blueprint('course', __name__)

# Add all students that are enrolled in moodle courses to the haski courses
@bp_course.route("/course/<course_id>/allStudents", methods=["POST"])
@cross_origin(supports_credentials=True)
def add_all_students_to_course(course_id):
    method = request.method
    match method:
        case "POST":
            created_for = []
            students = services.get_all_students(unit_of_work.SqlAlchemyUnitOfWork())
            for student in students:
                user = services.get_user_by_id(
                    unit_of_work.SqlAlchemyUnitOfWork(), student["user_id"], None
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
                jsonify({"CREATED": False, "course_id": course_id, "student_count": 0}),
                http.HTTPStatus.NOT_FOUND,
            )

# Add Topic to course and add all students to it
@bp_course.route("/course/<course_id>/topics/allStudents", methods=["POST"])
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
                    services.add_student_to_topics(uow, student["id"], course_id)
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
                jsonify({"CREATED": False, "course_id": course_id, "student_count": 0}),
                http.HTTPStatus.NOT_FOUND,
            )
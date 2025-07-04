import json
from unittest import mock

import pytest

import utils.constants as const

user_id_admin = 0
admin_id = 0
user_id_course_creator = 0
course_creator_id = 0
user_id_teacher = 0
teacher_id = 0
user_id_student = 0
student_id = 0
lms_user_id_admin = 1
lms_user_id_creator = 2
lms_user_id_teacher = 3
lms_user_id_student = 4
course_id = 0
topic_id = 0
sub_topic_id = 0
learning_element_id = 0
questionnaire_ils_id = 0
questionnaire_list_k_id = 0

path_admin = "/admin"
path_activity_status = "/activitystatus"
path_course = "/course"
path_courses = "/courses"
path_contactform = "/contactform"
path_content = "/content"
path_news = "/news"
path_logbuffer = "/logbuffer"
path_knowledge = "/knowledge"
path_logs = "/logs"
path_frontend_logs = "/logs/frontend"
path_learning_analytics = "/learningAnalytics"
path_learning_characteristics = "/learningCharacteristics"
path_learning_element = "/learningElement"
path_learning_path = "/learningPath"
path_learning_strategy = "/learningStrategy"
path_learning_style = "/learningStyle"
path_lms_course = "/lms/course"
path_lms_topic = "/lms/topic"
path_lms_student = "/lms/student"
path_lms_user = "/lms/user"
path_lms_learning_element = "/lms/learningElement"
path_questionnaire_ils = "/questionnaire/ils"
path_questionnaire_list_k = "/questionnaire/listk"
path_recommendation = "/recommendation"
path_remote = "/lms/remote"
path_settings = "/settings"
path_student = "/student"
path_subtopic = "/subtopic"
path_teacher = "/teacher"
path_topic = "/topic"
path_user = "/user"
path_algorithm = "/algorithm"
path_student_algorithm = "/studentAlgorithm"
path_teacher_algorithm = "/teacherAlgorithm"
path_rating = "/rating"

ils_complete = [
    "ar_1_f1",
    "ar_2_f5",
    "ar_3_f9",
    "ar_4_f13",
    "ar_5_f17",
    "ar_6_f21",
    "ar_7_f25",
    "ar_8_f29",
    "ar_9_f33",
    "ar_10_f37",
    "ar_11_f41",
    "si_1_f2",
    "si_2_f6",
    "si_3_f10",
    "si_4_f14",
    "si_5_f18",
    "si_6_f22",
    "si_7_f26",
    "si_8_f30",
    "si_9_f34",
    "si_10_f38",
    "si_11_f42",
    "vv_1_f3",
    "vv_2_f7",
    "vv_3_f11",
    "vv_4_f15",
    "vv_5_f19",
    "vv_6_f23",
    "vv_7_f27",
    "vv_8_f31",
    "vv_9_f35",
    "vv_10_f39",
    "vv_11_f43",
    "sg_1_f4",
    "sg_2_f8",
    "sg_3_f12",
    "sg_4_f16",
    "sg_5_f20",
    "sg_6_f24",
    "sg_7_f28",
    "sg_8_f32",
    "sg_9_f36",
    "sg_10_f40",
    "sg_11_f44",
]
ils_short = [
    "ar_3_f9",
    "ar_4_f13",
    "ar_6_f21",
    "ar_7_f25",
    "ar_8_f29",
    "si_1_f2",
    "si_4_f14",
    "si_7_f26",
    "si_10_f38",
    "si_11_f42",
    "vv_2_f7",
    "vv_5_f19",
    "vv_7_f27",
    "vv_10_f39",
    "vv_11_f43",
    "sg_1_f4",
    "sg_2_f8",
    "sg_4_f16",
    "sg_10_f40",
    "sg_11_f44",
]
list_k_ids = [
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
wrong_test_id = "Test ID"


# fixtures


# def predefined_users(client):
#     client_class.post(
#         path_lms_user,
#         json={
#             "name": "Achim Admin",
#             "lms_user_id": 1,
#             "role": "Admin",
#             "university": "TH-AB",
#             "password": "password",
#         },
#     )
#     client_class.post(
#         path_lms_user,
#         json={
#             "name": "Claus Creator",
#             "lms_user_id": 2,
#             "role": "Course Creator",
#             "university": "TH-AB",
#             "password": "password",
#         },
#     )
#     client_class.post(
#         path_lms_user,
#         json={
#             "name": "Tim Teacher",
#             "lms_user_id": 3,
#             "role": "Teacher",
#             "university": "TH-AB",
#             "password": "password",
#         },
#     )
#     client_class.post(
#         path_lms_user,
#         json={
#             "name": "Sonja Studentin",
#             "lms_user_id": 4,
#             "role": "Student",
#             "university": "TH-AB",
#             "password": "password",
#         },
#     )


# def fill_globals(r):
#     response = json.loads(r.data.decode("utf-8").strip("\n"))
#     user_id = response["id"]
#     role_id = response["role_id"]
#     return user_id, role_id
# Class setup
@pytest.mark.usefixtures("client")
@pytest.fixture(scope="session", name="client_class")
def client(client):
    return client


global_client_class = None


@pytest.fixture(scope="session")
@pytest.mark.usefixtures("client_class")
def client_class(client_class):
    global global_client_class
    if global_client_class is None:
        global_client_class = client_class
    return global_client_class


class TestApi:
    # POST METHODS
    # Create User
    @pytest.mark.parametrize(
        "input, keys_expected, status_code_expected,\
                            save_id",
        [
            # Working Example Admin
            (
                {
                    "name": "Achim Admin",
                    "lms_user_id": lms_user_id_admin,
                    "role": "Admin",
                    "university": "TH-AB",
                    "password": "password",
                },
                [
                    "id",
                    "name",
                    "university",
                    "lms_user_id",
                    "role",
                    "role_id",
                    "settings",
                ],
                201,
                True,
            ),
            # Working Example Course Creator
            (
                {
                    "name": "Claus Creator",
                    "lms_user_id": lms_user_id_creator,
                    "role": "Course Creator",
                    "university": "TH-AB",
                    "password": "password",
                },
                [
                    "id",
                    "name",
                    "university",
                    "lms_user_id",
                    "role",
                    "role_id",
                    "settings",
                ],
                201,
                True,
            ),
            # Working Example Teacher
            (
                {
                    "name": "Tim Teacher",
                    "lms_user_id": lms_user_id_teacher,
                    "role": "Teacher",
                    "university": "TH-AB",
                    "password": "password",
                },
                [
                    "id",
                    "name",
                    "university",
                    "lms_user_id",
                    "role",
                    "role_id",
                    "settings",
                ],
                201,
                True,
            ),
            # Working Example Student
            (
                {
                    "name": "Sonja Studentin",
                    "lms_user_id": lms_user_id_student,
                    "role": "Student",
                    "university": "TH-AB",
                    "password": "password",
                },
                [
                    "id",
                    "name",
                    "university",
                    "lms_user_id",
                    "role",
                    "role_id",
                    "settings",
                ],
                201,
                True,
            ),
            # Missing Parameter
            (
                {
                    "lms_user_id": 1,
                    "role": "Student",
                    "university": "TH-AB",
                    "password": "password",
                },
                ["error", "message"],
                400,
                False,
            ),
            # Parameter with wrong data type
            (
                {
                    "name": "Max Mustermann",
                    "lms_user_id": "1",
                    "role": "Student",
                    "university": "TH-AB",
                    "password": "password",
                },
                ["error", "message"],
                400,
                False,
            ),
            # User already exists
            (
                {
                    "name": "Achim Admin",
                    "lms_user_id": 1,
                    "role": "Admin",
                    "university": "TH-AB",
                    "password": "password",
                },
                ["error", "message"],
                400,
                False,
            ),
        ],
    )
    def test_api_create_user_from_moodle(
        self, client_class, input, keys_expected, status_code_expected, save_id
    ):
        url = path_lms_user
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()
        if save_id:
            match input["role"].lower():
                case const.role_admin_string:
                    global user_id_admin, admin_id
                    user_id_admin = response["id"]
                    admin_id = response["role_id"]
                case const.role_course_creator_string:
                    global user_id_course_creator, course_creator_id
                    user_id_course_creator = response["id"]
                    course_creator_id = response["role_id"]
                case const.role_teacher_string:
                    global user_id_teacher, teacher_id
                    user_id_teacher = response["id"]
                    teacher_id = response["role_id"]
                case const.role_student_string:
                    global user_id_student, student_id
                    user_id_student = response["id"]
                    student_id = response["role_id"]

    # Create Course
    @pytest.mark.parametrize(
        "input, keys_expected, status_code_expected,\
                            save_id",
        [
            # Working Example
            (
                {
                    "name": "Test Course",
                    "lms_id": 1,
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                ["id", "name", "lms_id", "created_at", "created_by", "university"],
                201,
                True,
            ),
            # Missing Parameter
            (
                {"name": "Test Course", "university": "TH-AB"},
                ["error", "message"],
                400,
                False,
            ),
            # Parameter with wrong data type
            (
                {
                    "name": "Test Course",
                    "lms_id": "1",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                ["error", "message"],
                400,
                False,
            ),
            # Course already exists
            (
                {
                    "name": "Test Course",
                    "lms_id": 1,
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                ["error", "message"],
                400,
                False,
            ),
        ],
    )
    def test_api_create_course_from_moodle_without_start_date(
        self, client_class, input, keys_expected, status_code_expected, save_id
    ):
        global user_id_course_creator
        input["created_by"] = user_id_course_creator
        url = path_lms_course
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()
        if save_id:
            global course_id
            course_id = response["id"]

    @pytest.mark.parametrize(
        "input, keys_expected, status_code_expected,\
                            save_id",
        [
            # Working Example
            (
                {
                    "name": "Test Course without start date",
                    "lms_id": 2,
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                    "start_date": "2023-08-01T13:37:42Z",
                },
                [
                    "id",
                    "name",
                    "lms_id",
                    "created_at",
                    "created_by",
                    "university",
                    "start_date",
                ],
                201,
                True,
            ),
            # Missing Parameter
            (
                {"name": "Test Course", "university": "TH-AB"},
                ["error", "message"],
                400,
                False,
            ),
            # Parameter with wrong data type
            (
                {
                    "name": "Test Course",
                    "lms_id": "2",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                    "start_date": "2023-08-01T13:37:42Z",
                },
                ["error", "message"],
                400,
                False,
            ),
            # Course already exists
            (
                {
                    "name": "Test Course",
                    "lms_id": 2,
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                    "start_date": "2023-08-01T13:37:42Z",
                },
                ["error", "message"],
                400,
                False,
            ),
        ],
    )
    def test_api_create_course_from_moodle(
        self, client_class, input, keys_expected, status_code_expected, save_id
    ):
        global user_id_course_creator
        input["created_by"] = user_id_course_creator
        url = path_lms_course
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()
        if save_id:
            global course_id
            course_id = response["id"]

    # Create Topic
    @pytest.mark.parametrize(
        "input, moodle_course_id, \
                            keys_expected, status_code_expected, save_id",
        [
            # Working Example for Topic
            (
                {
                    "name": "Test Topic",
                    "lms_id": 1,
                    "is_topic": True,
                    "contains_le": False,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                [
                    "id",
                    "name",
                    "lms_id",
                    "is_topic",
                    "parent_id",
                    "contains_le",
                    "created_by",
                    "created_at",
                    "university",
                ],
                201,
                True,
            ),
            # Working Example for Sub-Topic
            (
                {
                    "name": "Test Sub-Topic",
                    "lms_id": 2,
                    "is_topic": False,
                    "parent_id": 1,
                    "contains_le": True,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                [
                    "id",
                    "name",
                    "lms_id",
                    "is_topic",
                    "parent_id",
                    "contains_le",
                    "created_by",
                    "created_at",
                    "university",
                ],
                201,
                True,
            ),
            # Missing Parameter
            (
                {
                    "name": "Test Topic",
                    "is_topic": True,
                    "contains_le": False,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                ["error", "message"],
                400,
                False,
            ),
            # Parameter with wrong data type
            (
                {
                    "name": "Test Topic",
                    "lms_id": "1",
                    "is_topic": True,
                    "contains_le": False,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                ["error", "message"],
                400,
                False,
            ),
            # Topic already exists
            (
                {
                    "name": "Test Topic",
                    "lms_id": 1,
                    "is_topic": True,
                    "contains_le": False,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                ["error", "message"],
                400,
                False,
            ),
        ],
    )
    def test_api_create_topic_from_moodle(
        self,
        client_class,
        input,
        moodle_course_id,
        keys_expected,
        status_code_expected,
        save_id,
    ):
        global course_id, topic_id, sub_topic_id
        url = path_lms_course + "/" + str(course_id) + path_topic
        if topic_id != 0:
            input["parent_id"] = topic_id
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()
        if save_id:
            if "parent_id" in input.keys():
                sub_topic_id = response["id"]
            else:
                topic_id = response["id"]

    # Create Learning Element
    @pytest.mark.parametrize(
        "input, moodle_course_id,\
                            moodle_topic_id, keys_expected, \
                            status_code_expected, save_id",
        [
            # Working Example for LE
            (
                {
                    "lms_id": 1,
                    "activity_type": "Quiz",
                    "classification": "ÜB",
                    "name": "Test Learning Element",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                1,
                [
                    "id",
                    "lms_id",
                    "activity_type",
                    "classification",
                    "name",
                    "created_by",
                    "created_at",
                    "university",
                ],
                201,
                True,
            ),
            # Missing Parameter
            (
                {
                    "lms_id": 1,
                    "classification": "RQ",
                    "name": "Test Learning Element",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                1,
                ["error", "message"],
                400,
                False,
            ),
            # Parameter with wrong data type
            (
                {
                    "lms_id": "1",
                    "activity_type": "Quiz",
                    "classification": "RQ",
                    "name": "Test Learning Element",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                1,
                ["error", "message"],
                400,
                False,
            ),
            # LE already exists
            (
                {
                    "lms_id": 1,
                    "activity_type": "Quiz",
                    "classification": "ÜB",
                    "name": "Test Learning Element",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "university": "TH-AB",
                },
                1,
                1,
                ["error", "message"],
                400,
                False,
            ),
        ],
    )
    def test_api_create_le_from_moodle(
        self,
        client_class,
        input,
        moodle_course_id,
        moodle_topic_id,
        keys_expected,
        status_code_expected,
        save_id,
    ):
        global course_id
        global sub_topic_id
        url = path_lms_topic + "/" + str(sub_topic_id) + path_learning_element
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()
        if save_id:
            global learning_element_id
            learning_element_id = response["id"]

    # Add Teacher to Course
    @pytest.mark.parametrize(
        "error_teacher, error_course, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (False, False, ["id", "course_id", "teacher_id"], 201),
            # Teacher not found
            (True, False, ["error", "message"], 404),
            # Course not found
            (False, True, ["error", "message"], 404),
            # Teacher already in Course
            (False, False, ["error", "message"], 400),
        ],
    )
    def test_add_teacher_to_course(
        self,
        client_class,
        error_teacher,
        error_course,
        keys_expected,
        status_code_expected,
    ):
        global course_id, teacher_id
        if error_teacher:
            teacher_id_use = 99999
        else:
            teacher_id_use = teacher_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        url = (
            path_lms_course
            + "/"
            + str(course_id_use)
            + path_teacher
            + "/"
            + str(teacher_id_use)
        )
        r = client_class.post(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Add Student to Course
    @pytest.mark.parametrize(
        "error_student, error_course, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                False,
                False,
                [
                    "id",
                    "course_id",
                    "student_id",
                    "input_dimension",
                    "input_value",
                    "perception_dimension",
                    "perception_value",
                    "processing_dimension",
                    "processing_value",
                    "understanding_dimension",
                    "understanding_value",
                ],
                201,
            ),
            # Student not found
            (True, False, ["error", "message"], 404),
            # Course not found
            (False, True, ["error", "message"], 404),
            # Student already in Course
            (False, False, ["error", "message"], 400),
        ],
    )
    def test_add_student_to_course(
        self,
        client_class,
        error_student,
        error_course,
        keys_expected,
        status_code_expected,
    ):
        global course_id, student_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        url = (
            path_lms_course
            + "/"
            + str(course_id_use)
            + path_student
            + "/"
            + str(student_id_use)
        )
        r = client_class.post(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    @pytest.mark.parametrize(
        "input, keys_expected, status_code_expected",
        [
            (
                {"short_name": "aco", "full_name": "Ant Colony Optimization"},
                ["full_name", "id", "short_name"],
                201,
            ),
        ],
    )
    def test_post_learning_path_algorithm(
        self, client_class, input, keys_expected, status_code_expected
    ):
        url = path_algorithm
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Test post to create student learning path learning element algorithm
    @pytest.mark.parametrize(
        "input, topic_id, keys_expected, status_code_expected",
        [
            (
                {"algorithm": "aco"},
                1,
                ["algorithm_id", "id", "student_id", "topic_id"],
                201,
            ),
            (
                {"algorithm": "aco"},
                2,
                ["algorithm_id", "id", "student_id", "topic_id"],
                201,
            ),
        ],
    )
    def test_post_student_learning_path_learning_element_algorithm(
        self, client_class, input, topic_id, keys_expected, status_code_expected
    ):
        global student_id

        url = (
            path_student
            + "/"
            + str(student_id)
            + path_topic
            + "/"
            + str(topic_id)
            + path_algorithm
        )

        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Test post to create teacher learning path learning element algorithm
    @pytest.mark.parametrize(
        "input, user_id, lms_id, topic_id, keys_expected, status_code_expected",
        [
            (
                {"algorithm_short_name": "aco"},
                3,
                lms_user_id_teacher,
                1,
                ["algorithm_id", "topic_id"],
                201,
            ),
            (
                {"algorithm_short_name": "aco"},
                3,
                lms_user_id_teacher,
                1,
                ["algorithm_id", "topic_id"],
                201,
            ),
            # Wrong key
            (
                {"wrong_key": "algorithm"},
                3,
                lms_user_id_teacher,
                1,
                ["error", "message"],
                400,
            ),
            # Wrong data type
            (
                {"algorithm_short_name": 2},
                3,
                lms_user_id_teacher,
                1,
                ["error", "message"],
                400,
            ),
            # Unauthorized User
            (
                {"algorithm_short_name": "aco"},
                4,
                lms_user_id_student,
                1,
                ["error", "message"],
                401,
            ),
        ],
    )
    def test_post_teacher_learning_path_learning_element_algorithm(
        self,
        client_class,
        input,
        user_id,
        lms_id,
        topic_id,
        keys_expected,
        status_code_expected,
    ):
        url = (
            path_user
            + "/"
            + str(user_id)
            + "/"
            + str(lms_id)
            + path_topic
            + "/"
            + str(topic_id)
            + path_teacher_algorithm
        )

        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Test post to create student learning path learning element algorithm
    @pytest.mark.parametrize(
        "input, topic_id, keys_expected, status_code_expected",
        [
            (
                {"algorithm_short_name": "aco"},
                1,
                ["algorithm_id", "id", "student_id", "topic_id"],
                201,
            ),
            (
                {"algorithm_short_name": "aco"},
                1,
                ["algorithm_id", "id", "student_id", "topic_id"],
                201,
            ),
            (
                {"wrong_key": "algorithm"},
                1,
                ["error", "message"],
                400,
            ),
            (
                {"algorithm_short_name": 2},
                1,
                ["error", "message"],
                400,
            ),
        ],
    )
    def test_p_student_learning_path_learning_element_algorithm(
        self, client_class, input, topic_id, keys_expected, status_code_expected
    ):
        global user_id_student

        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(4)
            + path_course
            + "/"
            + str(course_id)
            + path_topic
            + "/"
            + str(sub_topic_id)
            + path_student_algorithm
        )
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Post Questionnaire for Student
    @pytest.mark.parametrize(
        "student_id, keys_expected, status_code_expected, \
         save_id, error_id_missing, error_answer_list_k, error_list_k_id",
        [
            # Working example
            (
                1,
                [
                    "att",
                    "characteristic_id",
                    "cogn_str",
                    "con",
                    "crit_rev",
                    "eff",
                    "elab",
                    "ext_res_mng_str",
                    "goal_plan",
                    "id",
                    "int_res_mng_str",
                    "lit_res",
                    "lrn_env",
                    "lrn_w_cls",
                    "metacogn_str",
                    "org",
                    "reg",
                    "rep",
                    "time",
                ],
                201,
                True,
                False,
                False,
                False,
            ),
            # Missing mandatory answer
            (1, ["error", "message"], 400, False, True, False, False),
            # Wrong answer type LIST-K
            (1, ["error", "message"], 400, False, False, True, False),
            # Wrong question ID for LIST-K
            (1, ["error", "message"], 400, False, False, False, True),
        ],
    )
    def test_post_questionnaire_list_k(
        self,
        client_class,
        student_id,
        keys_expected,
        status_code_expected,
        save_id,
        error_id_missing,
        error_answer_list_k,
        error_list_k_id,
    ):
        json_input = {}
        list_k = []
        for id in list_k_ids:
            temp = {}
            if error_list_k_id:
                temp["question_id"] = wrong_test_id
            else:
                temp["question_id"] = id
            if error_answer_list_k:
                temp["answer"] = 7
            else:
                temp["answer"] = 1
            if error_id_missing:
                temp["question_id"] = ""
            list_k.append(temp)
        json_input["list_k"] = list_k

        url = path_lms_student + "/" + str(student_id) + path_questionnaire_list_k
        r = client_class.post(url, json=json_input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            print(response.keys())
            assert key in response.keys()
        if save_id:
            global questionnaire_list_k_id
            questionnaire_list_k_id = response["id"]

    @pytest.mark.parametrize(
        "ils_long, student_id, keys_expected, status_code_expected, \
         save_id, error_id_missing, error_key_wrong, error_answer_ils,",
        [
            # Working example
            (
                True,
                1,
                [
                    "characteristic_id",
                    "id",
                    "input_dimension",
                    "input_value",
                    "perception_dimension",
                    "perception_value",
                    "processing_dimension",
                    "processing_value",
                    "understanding_dimension",
                    "understanding_value",
                ],
                201,
                True,
                False,
                False,
                False,
            ),
            # Working example short questionnaire
            (
                False,
                1,
                [
                    "characteristic_id",
                    "id",
                    "input_dimension",
                    "input_value",
                    "perception_dimension",
                    "perception_value",
                    "processing_dimension",
                    "processing_value",
                    "understanding_dimension",
                    "understanding_value",
                ],
                201,
                True,
                False,
                False,
                False,
            ),
            # Missing mandatory answer
            (False, 1, ["error", "message"], 400, False, True, False, False),
            # Wrong ID for question
            (True, 1, ["error", "message"], 400, False, False, True, False),
            # Wrong answer type for ILS
            (True, 1, ["error", "message"], 400, False, False, False, True),
        ],
    )
    def test_post_questionnaire_ils(
        self,
        client_class,
        ils_long,
        student_id,
        keys_expected,
        status_code_expected,
        save_id,
        error_id_missing,
        error_key_wrong,
        error_answer_ils,
    ):
        json_input = {}
        ils = []
        if ils_long:
            for id in ils_complete:
                temp = {}
                if error_key_wrong:
                    temp["question_id"] = wrong_test_id
                else:
                    temp["question_id"] = id
                if error_answer_ils:
                    temp["answer"] = "c"
                else:
                    temp["answer"] = "a"
                ils.append(temp)
            json_input["ils"] = ils
        elif error_id_missing:
            json_input["ils"] = ils
        else:
            for id in ils_short:
                temp = {}
                if error_key_wrong:
                    temp["question_id"] = wrong_test_id
                else:
                    temp["question_id"] = id
                if error_answer_ils:
                    temp["answer"] = "c"
                else:
                    temp["answer"] = "a"
                ils.append(temp)
            json_input["ils"] = ils

        url = path_lms_student + "/" + str(student_id) + path_questionnaire_ils
        r = client_class.post(url, json=json_input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()
        if save_id:
            global questionnaire_ils_id
            questionnaire_ils_id = response["id"]

    # Student visits Topic
    @pytest.mark.parametrize(
        "input,  moodle_user_id, \
                            keys_expected, status_code_expected",
        [
            # Working Example
            (
                {"visit_start": "2023-08-01T13:37:42Z"},
                4,
                ["id", "student_id", "topic_id", "visit_start", "visit_end"],
                201,
            ),
            # Wrong data format
            ({"visit_start": "01.01.2023"}, 4, ["error", "message"], 400),
            # Missing Parameter
            ({"previous_topic_id": 1}, 4, ["error", "message"], 400),
        ],
    )
    def test_post_topic_visit(
        self, client_class, input, moodle_user_id, keys_expected, status_code_expected
    ):
        global student_id, topic_id
        url = (
            path_lms_student
            + "/"
            + str(student_id)
            + "/"
            + str(moodle_user_id)
            + path_topic
            + "/"
            + str(topic_id)
        )
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Student visits Learning Element
    @pytest.mark.parametrize(
        "input, moodle_user_id, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                {"visit_start": "2023-08-01T13:37:42Z"},
                4,
                ["student_id", "learning_element_id", "visit_start", "visit_end"],
                201,
            ),
            # Wrong data format
            ({"visit_start_time": "01.01.2023"}, 4, ["error", "message"], 400),
            # Missing Parameter
            ({"previous_learning_element_id": 1}, 4, ["error", "message"], 400),
        ],
    )
    def test_post_learning_element_visit(
        self, client_class, input, moodle_user_id, keys_expected, status_code_expected
    ):
        global student_id, learning_element_id
        url = (
            path_lms_student
            + "/"
            + str(student_id)
            + "/"
            + str(moodle_user_id)
            + path_learning_element
            + "/"
            + str(learning_element_id)
        )
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Learning Path is calculated
    @pytest.mark.parametrize(
        "input, moodle_user_id, keys_expected,\
                            status_code_expected",
        [
            # Working Example ACO
            (
                {"algorithm": "aco"},
                4,
                [
                    "id",
                    "course_id",
                    "topic_id",
                    "student_id",
                    "based_on",
                    "path",
                    "calculated_on",
                ],
                201,
            ),
            # Working Example Graf
            (
                {"algorithm": "graf"},
                4,
                [
                    "id",
                    "course_id",
                    "topic_id",
                    "student_id",
                    "based_on",
                    "path",
                    "calculated_on",
                ],
                201,
            ),
            # Missing Parameter
            ({}, 4, ["error", "message"], 400),
        ],
    )
    def test_post_learning_path(
        self, client_class, input, moodle_user_id, keys_expected, status_code_expected
    ):
        global user_id_student, student_id, course_id, sub_topic_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(moodle_user_id)
            + path_student
            + "/"
            + str(student_id)
            + path_course
            + "/"
            + str(course_id)
            + path_topic
            + "/"
            + str(sub_topic_id)
            + path_learning_path
        )
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Learning Path is calculated for ga
    @pytest.mark.parametrize(
        "input, moodle_user_id, keys_exp,\
                            status_code_exp",
        [
            # Working Example
            (
                {"algorithm": "ga"},
                4,
                [
                    "id",
                    "course_id",
                    "topic_id",
                    "student_id",
                    "based_on",
                    "path",
                    "calculated_on",
                ],
                201,
            ),
            # Missing Parameter
            ({}, 4, ["error", "message"], 400),
        ],
    )
    def test_post_learning_path_ga(
        self, client_class, input, moodle_user_id, keys_exp, status_code_exp
    ):
        global user_id_student, student_id, course_id2, sub_topic_id2
        client_post = client_class.post(
            (
                path_user
                + "/"
                + str(user_id_student)
                + "/"
                + str(moodle_user_id)
                + path_student
                + "/"
                + str(student_id)
                + path_course
                + "/"
                + str(course_id)
                + path_topic
                + "/"
                + str(sub_topic_id)
                + path_learning_path
            ),
            json=input,
        )
        assert client_post.status_code == status_code_exp
        response = json.loads(client_post.data.decode("utf-8").strip("\n"))
        for key in keys_exp:
            assert key in response.keys()

    # Default Learning Path is calculated
    @pytest.mark.parametrize(
        "input, moodle_user_id, keys_exp,\
                            status_code_exp",
        [
            # Working Example
            (
                [
                    {
                        "classification": "KÜ",
                        "position": 1,
                        "disabled": False,
                        "university": "HS-KE",
                    }
                ],
                1,
                ["classification", "position", "disabled", "university"],
                201,
            ),
            (
                [
                    {
                        "classification": "EK",
                        "position": 1,
                        "disabled": False,
                        "university": "HS-KE",
                    }
                ],
                1,
                ["classification", "position", "disabled", "university"],
                201,
            ),
            # Missing Parameter
            ({}, 1, ["error", "message"], 500),
        ],
    )
    def test_post_learning_path_default(
        self, client_class, input, moodle_user_id, keys_exp, status_code_exp
    ):
        global user_id_student, student_id, course_id2, sub_topic_id2
        client_post = client_class.post(
            (
                path_user
                + "/"
                + str(user_id_admin)
                + "/"
                + str(moodle_user_id)
                + "/defaultLearningPath"
            ),
            json=input,
        )
        assert client_post.status_code == status_code_exp
        response = json.loads(client_post.data.decode("utf-8").strip("\n"))
        if input == {}:
            expected_keys = set(["error", "message"])
            assert expected_keys <= set(response.keys())
        else:
            for item in response:
                assert set(keys_exp) <= set(item.keys())

    @pytest.mark.parametrize(
        "moodle_user_id, keys_exp, status_code_exp",
        [
            # Working Example
            (
                1,
                ["id", "classification", "position", "disabled", "university"],
                200,
            ),
        ],
    )
    def test_get_learning_path_default(
        self, client_class, moodle_user_id, keys_exp, status_code_exp
    ):
        global user_id_student, student_id, course_id2, sub_topic_id2
        client_get = client_class.get(
            path_user
            + "/"
            + str(user_id_admin)
            + "/"
            + str(moodle_user_id)
            + "/defaultLearningPath"
        )
        assert client_get.status_code == status_code_exp
        response = json.loads(client_get.data.decode("utf-8").strip("\n"))
        if input == {}:
            expected_keys = set(["error", "message"])
            assert expected_keys <= set(response.keys())
        else:
            for item in response:
                assert set(keys_exp) <= set(item.keys())

    # Learning paths are calculated
    @pytest.mark.parametrize(
        "input, moodle_user_id, keys_expected,\
                            status_code_expected",
        [
            (
                {},
                4,
                [
                    "id",
                    "course_id",
                    "topic_id",
                    "student_id",
                    "based_on",
                    "path",
                    "calculated_on",
                ],
                201,
            ),
        ],
    )
    def test_post_calculate_learning_path(
        self, client_class, input, moodle_user_id, keys_expected, status_code_expected
    ):
        user_id_student = 4
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(moodle_user_id)
            + path_learning_path
        )
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        responses = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            for response in responses:
                assert key in response.keys()

    # Learning paths are calculated for all students
    @pytest.mark.parametrize(
        "input, moodle_user_id, keys_expected, status_code_expected",
        [
            (
                {
                    "university": "TH-AB",  # Added required key
                    "role": "teacher",  # Added required key
                },
                4,
                [
                    "id",
                    "course_id",
                    "topic_id",
                    "student_id",
                    "based_on",
                    "path",
                    "calculated_on",
                ],
                201,
            ),
        ],
    )
    def test_post_calculate_learning_path_for_all_students(
        self, client_class, input, moodle_user_id, keys_expected, status_code_expected
    ):
        global user_id_course_creator, course_id, sub_topic_id, user_id_student
        url = (
            "/v2"
            + path_user
            + "/"
            + str(user_id_student)
            + path_course
            + "/"
            + str(course_id)
            + path_topic
            + "/"
            + str(1)
            + path_learning_path
        )
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        responses = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            for response in responses:
                assert key in response.keys()
        # Save course_id if needed
        # if save_id:
        #     global course_id
        #     course_id = responses[0]["id"]

    @pytest.mark.parametrize(
        "keys_expected, status_code_expected",
        [
            (
                {
                    "id",
                    "student_id",
                    "topic_id",
                    "rating_value",
                    "rating_deviation",
                    "timestamp",
                },
                201,
            ),
        ],
    )
    def test_create_student_rating(
        self, client_class, keys_expected, status_code_expected
    ):
        url = (
            path_student
            + "/"
            + str(student_id)
            + path_topic
            + "/"
            + str(topic_id)
            + path_rating
        )
        r = client_class.post(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    @pytest.mark.parametrize(
        "keys_expected, status_code_expected",
        [
            (
                {
                    "id",
                    "student_id",
                    "topic_id",
                    "rating_value",
                    "rating_deviation",
                    "timestamp",
                },
                200,
            ),
        ],
    )
    def test_get_student_ratings_on_topic(
        self, client_class, keys_expected, status_code_expected
    ):
        url = (
            path_student
            + "/"
            + str(student_id)
            + path_topic
            + "/"
            + str(topic_id)
            + path_rating
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response[0].keys():
            assert key in keys_expected

    @pytest.mark.parametrize(
        "keys_expected, status_code_expected",
        [
            (
                {
                    "id",
                    "student_id",
                    "topic_id",
                    "rating_value",
                    "rating_deviation",
                    "timestamp",
                },
                200,
            ),
        ],
    )
    def test_get_student_ratings(
        self, client_class, keys_expected, status_code_expected
    ):
        user_id_student = 4
        student_id = 2
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + path_student
            + "/"
            + str(student_id)
            + path_rating
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response[0].keys():
            assert key in keys_expected

    @pytest.mark.parametrize(
        "keys_expected, status_code_expected",
        [
            (
                {
                    "id",
                    "learning_element_id",
                    "topic_id",
                    "rating_value",
                    "rating_deviation",
                    "timestamp",
                },
                201,
            ),
        ],
    )
    def test_create_learning_element_rating(
        self, client_class, keys_expected, status_code_expected
    ):
        url = (
            path_topic
            + "/"
            + str(topic_id)
            + path_learning_element
            + "/"
            + str(learning_element_id)
            + path_rating
        )
        r = client_class.post(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    @pytest.mark.parametrize(
        "keys_expected, status_code_expected",
        [
            (
                {
                    "id",
                    "learning_element_id",
                    "topic_id",
                    "rating_value",
                    "rating_deviation",
                    "timestamp",
                },
                200,
            ),
        ],
    )
    def test_get_learning_element_ratings_on_topic(
        self, client_class, keys_expected, status_code_expected
    ):
        url = (
            path_topic
            + "/"
            + str(topic_id)
            + path_learning_element
            + "/"
            + str(learning_element_id)
            + path_rating
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response[0].keys():
            assert key in keys_expected

    @pytest.mark.parametrize(
        "keys_expected, status_code_expected",
        [
            (
                {
                    "id",
                    "learning_element_id",
                    "topic_id",
                    "rating_value",
                    "rating_deviation",
                    "timestamp",
                },
                200,
            ),
        ],
    )
    def test_get_learning_element_ratings(
        self, client_class, keys_expected, status_code_expected
    ):
        url = path_learning_element + path_rating
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response[0].keys():
            assert key in keys_expected

    @mock.patch("requests.get")
    @pytest.mark.parametrize(
        "keys_expected, status_code_expected",
        [
            (
                {
                    "student_rating",
                    "learning_element_rating",
                },
                201,
            ),
        ],
    )
    def test_post_calculate_rating(
        self, mock_get, client_class, keys_expected, status_code_expected
    ):
        mock_response_1 = mock.Mock(
            status_code=200, json=lambda: [{"modules": [{"id": 1, "instance": 1}]}]
        )

        mock_response_2 = mock.Mock(
            status_code=200,
            json=lambda: {
                "usersattempts": [
                    {"attempts": [{"timecreated": 1}, {"timecreated": 9999999999}]}
                ]
            },
        )

        mock_get.side_effect = [mock_response_1, mock_response_2]

        user_id_student = 4
        learning_element_id = 1
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + path_course
            + "/"
            + str(course_id)
            + path_topic
            + "/"
            + str(topic_id)
            + path_learning_element
            + "/"
            + str(learning_element_id)
            + path_rating
        )
        r = client_class.post(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    # Post a Contact Form
    @pytest.mark.parametrize(
        "input, lms_user_id, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                {
                    "report_topic": "Lernelement",
                    "report_type": "Funktionalität",
                    "report_description": "Test",
                },
                4,
                [
                    "id",
                    "user_id",
                    "report_topic",
                    "report_type",
                    "report_description",
                ],
                201,
            ),
            # Missing Parameter
            ({}, 4, ["error", "message"], 400),
        ],
    )
    def test_post_contact_form(
        self, client_class, input, lms_user_id, keys_expected, status_code_expected
    ):
        user_id_student = 4
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_contactform
        )
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Post Frontend Logs
    @pytest.mark.parametrize(
        "input, keys_expected, status_code_expected",
        [
            # Working Example
            (
                {
                    "name": "FCP",
                    "value": 3957.6999999284744,
                    "rating": "poor",
                    "delta": 3957.6999999284744,
                    "entries": [
                        {
                            "name": "first-contentful-paint",
                            "entryType": "paint",
                            "startTime": 3957.6999999284744,
                            "duration": 0,
                        },
                        {
                            "name": "http://localhost:8080/",
                            "entryType": "navigation",
                            "startTime": 0,
                            "duration": 4003.0999999046326,
                            "initiatorType": "navigation",
                            "nextHopProtocol": "http/1.1",
                            "workerStart": 0,
                            "redirectStart": 0,
                            "redirectEnd": 0,
                            "fetchStart": 7.699999928474426,
                            "domainLookupStart": 99.19999992847443,
                            "domainLookupEnd": 99.29999995231628,
                            "connectStart": 99.29999995231628,
                            "connectEnd": 99.89999997615814,
                            "secureConnectionStart": "0,",
                            "requestStart": 100,
                            "responseStart": 3638.7999999523163,
                            "responseEnd": 3640,
                            "transferSize": 810,
                            "encodedBodySize": 510,
                            "decodedBodySize": 510,
                            "serverTiming": [""],
                            "workerTiming": [""],
                            "unloadEventStart": 0,
                            "unloadEventEnd": 0,
                            "domInteractive": 3717.5,
                            "domContentLoadedEventStart": 3937.5999999046326,
                            "domContentLoadedEventEnd": 3938.899999976158,
                            "domComplete": 4003.0999999046326,
                            "loadEventStart": 4003.0999999046326,
                            "loadEventEnd": 4003.0999999046326,
                            "type": "navigate",
                            "redirectCount": 0,
                        },
                        {},
                        {
                            "name": "",
                            "entryType": "largest-contentful-paint",
                            "startTime": 3957.699,
                            "duration": 0,
                            "size": 867,
                            "renderTime": 3957.699,
                            "loadTime": 0,
                            "firstAnimatedFrameTime": 0,
                            "id": "",
                            "url": "",
                        },
                        {},
                        {},
                    ],
                    "id": "v3-1665068191217-4248786867866",
                    "navigationType": "navigate",
                },
                ["name", "value", "rating", "delta", "entries", "id", "navigationType"],
                201,
            )
        ],
    )
    def test_api_post_frontend_logs(
        self, client_class, input, keys_expected, status_code_expected
    ):
        url = path_frontend_logs
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Post the News
    @pytest.mark.parametrize(
        "input, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                {
                    "university": "TH-AB",
                    "language_id": "en",
                    "created_at": "2023-08-01T13:37:42Z",
                    "news_content": "This is news",
                    "expiration_date": "2028-08-01T13:37:42Z",
                },
                [
                    "id",
                    "university",
                    "created_at",
                    "language_id",
                    "expiration_date",
                    "news_content",
                ],
                201,
            ),
        ],
    )
    def test_post_news(self, client_class, input, keys_expected, status_code_expected):
        url = path_news
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Post the logbuffer
    @pytest.mark.parametrize(
        "input, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                {
                    "user_id": "4",
                    "content": "Test text",
                    "date": "2028-08-01T13:37:42Z",
                },
                [
                    "id",
                    "user_id",
                    "content",
                    "date",
                ],
                201,
            ),
            # Missing Parameter
            ({}, ["error", "message"], 400),
        ],
    )
    def test_post_logbuffer(
        self, client_class, input, keys_expected, status_code_expected
    ):
        user_id_student = 4
        url = path_user + "/" + str(user_id_student) + path_logbuffer
        r = client_class.post(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # GET METHODS
    # Get Students Learning Characteristics
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected, \
                            keys_expected, error",
        [
            # Working Example
            (
                4,
                200,
                [
                    "learning_style",
                    "learning_strategy",
                    "learning_analytics",
                    "knowledge",
                ],
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], True),
        ],
    )
    def test_get_students_learning_characteristics(
        self, client_class, lms_user_id, status_code_expected, keys_expected, error
    ):
        global user_id_student, student_id
        if error:
            student_id_use = 99999
        else:
            student_id_use = student_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_learning_characteristics
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get Learning Analytics
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected, \
                            keys_expected, error",
        [
            # Working Example
            (4, 200, [], False),
            # Student not found
            (1, 404, ["error", "message"], True),
        ],
    )
    def test_get_students_learning_analytics(
        self, client_class, lms_user_id, status_code_expected, keys_expected, error
    ):
        global user_id_student, student_id
        if error:
            student_id_use = 99999
        else:
            student_id_use = student_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_learning_analytics
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get Learning Style
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected, \
                            keys_expected, error",
        [
            # Working Example
            (
                4,
                200,
                [
                    "perception_dimension",
                    "perception_value",
                    "input_dimension",
                    "input_value",
                    "processing_dimension",
                    "processing_value",
                    "understanding_dimension",
                    "understanding_value",
                ],
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], True),
        ],
    )
    def test_get_students_learning_style(
        self, client_class, lms_user_id, status_code_expected, keys_expected, error
    ):
        global user_id_student, student_id
        if error:
            student_id_use = 99999
        else:
            student_id_use = student_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_learning_style
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get Learning Strategy
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected, \
                            keys_expected, error",
        [
            # Working Example
            (4, 200, [], False),
            # Student not found
            (1, 404, ["error", "message"], True),
        ],
    )
    def test_get_students_learning_strategy(
        self, client_class, lms_user_id, status_code_expected, keys_expected, error
    ):
        global user_id_student, student_id
        if error:
            student_id_use = 99999
        else:
            student_id_use = student_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_learning_strategy
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get Knowledge
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected, \
                            keys_expected, error",
        [
            # Working Example
            (4, 200, [], False),
            # Student not found
            (1, 404, ["error", "message"], True),
        ],
    )
    def test_get_students_knowledge(
        self, client_class, lms_user_id, status_code_expected, keys_expected, error
    ):
        global user_id_student, student_id
        if error:
            student_id_use = 99999
        else:
            student_id_use = student_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_knowledge
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get all courses for a student
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected, \
                            keys_expected_1, keys_expected_2, error",
        [
            # Working Example
            (4, 200, ["courses"], ["id", "lms_id", "name", "university"], False),
            # Student not found
            (1, 404, ["error", "message"], [], True),
        ],
    )
    def test_get_student_courses(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected_1,
        keys_expected_2,
        error,
    ):
        global user_id_student, student_id
        if error:
            student_id_use = 99999
        else:
            student_id_use = student_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        if "courses" in keys_expected_1:
            for key in keys_expected_1:
                assert key in response.keys()
            for key in keys_expected_2:
                assert key in response["courses"][0].keys()
        else:
            for key in keys_expected_1:
                assert key in response.keys()

    # Get a course for a student
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected, \
                            keys_expected, error_student,\
                            error_course",
        [
            # Working Example
            (4, 200, ["id", "name", "lms_id", "university"], False, False),
            # Student not found
            (1, 404, ["error", "message"], True, False),
            # Course not found
            (1, 404, ["error", "message"], False, True),
        ],
    )
    def test_get_student_course(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected,
        error_student,
        error_course,
    ):
        global user_id_student, student_id, course_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get all topics for a course
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected,\
                            keys_expected_1, keys_expected_2,\
                            error_student, error_course",
        [
            # Working Example
            (
                4,
                200,
                ["topics"],
                [
                    "id",
                    "lms_id",
                    "name",
                    "is_topic",
                    "contains_le",
                    "university",
                    "parent_id",
                    "student_topic",
                ],
                False,
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], [], True, False),
            # Course not found
            (1, 404, ["error", "message"], [], False, True),
        ],
    )
    def test_get_student_course_topics(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected_1,
        keys_expected_2,
        error_student,
        error_course,
    ):
        global user_id_student, student_id, course_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
            + path_topic
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        if "topics" in keys_expected_1:
            for key in keys_expected_1:
                assert key in response.keys()
            for key in keys_expected_2:
                assert key in response["topics"][0].keys()
        else:
            for key in keys_expected_1:
                assert key in response.keys()

    # Get all learning elements for a course
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected,\
                            keys_expected_1, keys_expected_2,\
                            error_student, error_course",
        [
            # Working Example
            (
                4,
                200,
                ["learning_elements"],
                [
                    "id",
                    "lms_id",
                    "activity_type",
                    "classification",
                    "name",
                    "university",
                    "student_learning_element",
                ],
                False,
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], [], True, False),
            # Course not found
            (1, 404, ["error", "message"], [], False, True),
        ],
    )
    def test_get_les_in_course_for_student(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected_1,
        keys_expected_2,
        error_student,
        error_course,
    ):
        global user_id_student, student_id, course_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
            + path_learning_element
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        if "topics" in keys_expected_1:
            for key in keys_expected_1:
                assert key in response.keys()
            for key in keys_expected_2:
                assert key in response["topics"][0].keys()
        else:
            for key in keys_expected_1:
                assert key in response.keys()

    # Get a specific topic in a course
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected,\
                            keys_expected, error_student,\
                            error_course, error_topic",
        [
            # Working Example
            (
                4,
                200,
                [
                    "id",
                    "lms_id",
                    "name",
                    "is_topic",
                    "contains_le",
                    "university",
                    "parent_id",
                    "student_topic",
                ],
                False,
                False,
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], True, False, False),
            # Course not found
            (1, 404, ["error", "message"], False, True, False),
            # Topic not found
            (1, 404, ["error", "message"], False, False, True),
        ],
    )
    def test_get_topic_by_id_for_student(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected,
        error_student,
        error_course,
        error_topic,
    ):
        global user_id_student, student_id, course_id, topic_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        if error_topic:
            topic_id_use = 99999
        else:
            topic_id_use = topic_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
            + path_topic
            + "/"
            + str(topic_id_use)
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get the recommended LE in a topic
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error_student,\
                            error_course, error_topic",
        [
            # Working Example
            (
                4,
                [
                    "id",
                    "lms_id",
                    "activity_type",
                    "classification",
                    "name",
                    "university",
                    "student_learning_element",
                ],
                200,
                False,
                False,
                False,
            ),
            # User not found
            (1, ["error", "message"], 404, True, False, False),
            # Course not found
            (4, ["error", "message"], 404, False, True, False),
            # Topic not found
            (4, ["error", "message"], 404, False, False, True),
        ],
    )
    def test_get_topic_recommendation_for_student(
        self,
        client_class,
        lms_user_id,
        keys_expected,
        status_code_expected,
        error_student,
        error_course,
        error_topic,
    ):
        global user_id_student, student_id, course_id, sub_topic_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        if error_topic:
            topic_id_use = 99999
        else:
            topic_id_use = sub_topic_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
            + path_topic
            + "/"
            + str(topic_id_use)
            + path_recommendation
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get the learning path for a topic
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected,\
                            keys_expected, error_student,\
                            error_course, error_topic",
        [
            # Working Example
            (
                4,
                200,
                [
                    "id",
                    "course_id",
                    "topic_id",
                    "student_id",
                    "based_on",
                    "calculated_on",
                    "path",
                ],
                False,
                False,
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], True, False, False),
            # Course not found
            (1, 404, ["error", "message"], False, True, False),
            # Topic not found
            (1, 404, ["error", "message"], False, False, True),
        ],
    )
    def test_get_learning_path_for_student(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected,
        error_student,
        error_course,
        error_topic,
    ):
        global user_id_student, student_id, course_id, sub_topic_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        if error_topic:
            topic_id_use = 99999
        else:
            topic_id_use = sub_topic_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
            + path_topic
            + "/"
            + str(topic_id_use)
            + path_learning_path
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get a Learning Path Algorithm that a teacher chose for a topic
    @pytest.mark.parametrize(
        "user_id, topic_id, keys_expected, status_code_expected",
        [
            (
                1,
                1,
                ["short_name", "algorithm_id", "topic_id"],
                200,
            ),
        ],
    )
    def test_get_learning_path_algorithm(
        self, client_class, user_id, topic_id, keys_expected, status_code_expected
    ):
        url = path_topic + "/" + str(topic_id) + path_teacher_algorithm
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get the learning path algorithm a student chose for a topic
    @pytest.mark.parametrize(
        "topic_id, keys_expected, status_code_expected",
        [
            (
                1,
                ["short_name", "algorithm_id", "topic_id"],
                200,
            ),
        ],
    )
    def test_get_learning_path_algorithm_student(
        self, client_class, topic_id, keys_expected, status_code_expected
    ):
        global user_id_student
        url = (
            path_user
            + "/"
            + str(4)
            + path_topic
            + "/"
            + str(topic_id)
            + path_student_algorithm
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get all sub-topics for a topic
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected,\
                            keys_expected_1, keys_expected_2,\
                            error_student, error_course, error_topic",
        [
            # Working Example
            (
                4,
                200,
                ["topics"],
                [
                    "id",
                    "lms_id",
                    "name",
                    "is_topic",
                    "contains_le",
                    "university",
                    "parent_id",
                    "student_topic",
                ],
                False,
                False,
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], [], True, False, False),
            # Course not found
            (1, 404, ["error", "message"], [], False, True, False),
            # Topic not found
            (1, 404, ["error", "message"], [], False, False, True),
        ],
    )
    def test_get_sub_topics_for_topic(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected_1,
        keys_expected_2,
        error_student,
        error_course,
        error_topic,
    ):
        global user_id_student, student_id, course_id, topic_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        if error_topic:
            topic_id_use = 99999
        else:
            topic_id_use = topic_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
            + path_topic
            + "/"
            + str(topic_id_use)
            + path_subtopic
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        if "topics" in keys_expected_1:
            for key in keys_expected_1:
                assert key in response.keys()
            for key in keys_expected_2:
                assert key in response["topics"][0].keys()
        else:
            for key in keys_expected_1:
                assert key in response.keys()

    # Get all LEs for a topic
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected,\
                            keys_expected_1, keys_expected_2,\
                            error_student, error_course,\
                            error_topic",
        [
            # Working Example
            (
                4,
                200,
                ["learning_elements"],
                [
                    "id",
                    "lms_id",
                    "activity_type",
                    "classification",
                    "name",
                    "university",
                    "student_learning_element",
                ],
                False,
                False,
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], [], True, False, False),
            # Course not found
            (1, 404, ["error", "message"], [], False, True, False),
            # Topic not found
            (1, 404, ["error", "message"], [], False, False, True),
        ],
    )
    def test_get_les_for_topic_for_student(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected_1,
        keys_expected_2,
        error_student,
        error_course,
        error_topic,
    ):
        global user_id_student, student_id, course_id, topic_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        if error_topic:
            topic_id_use = 99999
        else:
            topic_id_use = sub_topic_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
            + path_topic
            + "/"
            + str(topic_id_use)
            + path_learning_element
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        if "learning_elements" in keys_expected_1:
            for key in keys_expected_1:
                assert key in response.keys()
            for key in keys_expected_2:
                assert key in response["learning_elements"][0].keys()
        else:
            for key in keys_expected_1:
                assert key in response.keys()

    # Get a specific LE
    @pytest.mark.parametrize(
        "lms_user_id, status_code_expected,\
                            keys_expected, error_student,\
                            error_course, error_topic,\
                            error_le",
        [
            # Working Example
            (
                4,
                200,
                [
                    "id",
                    "lms_id",
                    "activity_type",
                    "classification",
                    "name",
                    "university",
                    "student_learning_element",
                ],
                False,
                False,
                False,
                False,
            ),
            # Student not found
            (1, 404, ["error", "message"], True, False, False, False),
            # Course not found
            (1, 404, ["error", "message"], False, True, False, False),
            # Topic not found
            (1, 404, ["error", "message"], False, False, True, False),
            # LE not found
            (1, 404, ["error", "message"], False, False, False, True),
        ],
    )
    def test_get_le_by_id_for_student(
        self,
        client_class,
        lms_user_id,
        status_code_expected,
        keys_expected,
        error_student,
        error_course,
        error_topic,
        error_le,
    ):
        global user_id_student, student_id, course_id
        global topic_id, learning_element_id
        if error_student:
            student_id_use = 99999
        else:
            student_id_use = student_id
        if error_course:
            course_id_use = 99999
        else:
            course_id_use = course_id
        if error_topic:
            topic_id_use = 99999
        else:
            topic_id_use = topic_id
        if error_le:
            learning_element_id_use = 99999
        else:
            learning_element_id_use = learning_element_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_course
            + "/"
            + str(course_id_use)
            + path_topic
            + "/"
            + str(topic_id_use)
            + path_learning_element
            + "/"
            + str(learning_element_id_use)
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get all Users by Admin
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected_1,\
                            keys_expected_2, status_code_expected,\
                            error_user",
        [
            # Working Example
            (1, ["users"], ["name", "role", "university"], 200, False),
            # User not found
            (1, ["error", "message"], [], 404, True),
        ],
    )
    def test_get_users_by_admin_id(
        self,
        client_class,
        lms_user_id,
        keys_expected_1,
        keys_expected_2,
        status_code_expected,
        error_user,
    ):
        global user_id_admin, admin_id
        if error_user:
            user_id_use = 99999
        else:
            user_id_use = user_id_admin
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_admin
            + "/"
            + str(admin_id)
            + path_user
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        if "users" in keys_expected_1:
            for key in keys_expected_2:
                assert key in response["users"][0].keys()
        else:
            for key in keys_expected_1:
                assert key in response.keys()

    # Get all logs by Admin
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error_admin",
        [
            # Working Example
            (1, ["logs"], 200, False),
            # User not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_get_logs_by_admin_id(
        self,
        client_class,
        lms_user_id,
        keys_expected,
        status_code_expected,
        error_admin,
    ):
        global user_id_admin, admin_id
        if error_admin:
            user_id_use = 99999
        else:
            user_id_use = user_id_admin
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_admin
            + "/"
            + str(admin_id)
            + path_logs
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get all courses by Teacher
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected_1,\
                            keys_expected_2, status_code_expected,\
                            error_teacher",
        [
            # Working Example
            (3, ["courses"], ["id", "name", "lms_id"], 200, False),
            # User not found
            (3, ["error", "message"], [], 404, True),
        ],
    )
    def test_get_courses_by_teacher_id(
        self,
        client_class,
        lms_user_id,
        keys_expected_1,
        keys_expected_2,
        status_code_expected,
        error_teacher,
    ):
        global user_id_teacher, teacher_id
        if error_teacher:
            user_id_use = 99999
        else:
            user_id_use = user_id_teacher
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_teacher
            + "/"
            + str(teacher_id)
            + path_course
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        if "courses" in keys_expected_1:
            for key in keys_expected_2:
                assert key in response["courses"][0].keys()
        else:
            for key in keys_expected_1:
                assert key in response.keys()

    # Get Remote Courses from LMS
    @mock.patch(
        "requests.get",
        mock.Mock(
            side_effect=lambda k: (
                mock.Mock(
                    status_code=200,
                    json=lambda: [
                        {
                            "id": 2,
                            "shortname": "SE - EM1 -SoSe23",
                            "fullname": "ω SE - Entwurfsmuster 1 - SoSe23",
                            "startdate": 1683759600,
                            "enddate": 0,
                            "timecreated": 1683723772,
                            "timemodified": 1699354676,
                        },
                        {
                            "id": 3,
                            "shortname": "tkh5p",
                            "fullname": "TestKurs-H5P",
                            "startdate": 1683846000,
                            "enddate": 1715382000,
                            "timecreated": 1683806079,
                            "timemodified": 1683806079,
                        },
                        {
                            "id": 4,
                            "shortname": "testcourse",
                            "fullname": "testcourse",
                            "startdate": 1688598000,
                            "enddate": 1720134000,
                            "timecreated": 1688566758,
                            "timemodified": 1688566758,
                        },
                        {
                            "id": 5,
                            "shortname": "SE - EM2 - WiSe23/24",
                            "fullname": "SE - Entwurfsmuster 2 - WiSe23/24",
                            "startdate": 1700611200,
                            "enddate": 1732233600,
                            "timecreated": 1699289698,
                            "timemodified": 1699354526,
                        },
                        {
                            "id": 6,
                            "shortname": "SE - EM1 - WiSe23/24",
                            "fullname": "SE - Entwurfsmuster 1 - WiSe23/24",
                            "startdate": 1699315200,
                            "enddate": 0,
                            "timecreated": 1683723772,
                            "timemodified": 1699354114,
                        },
                    ],
                )
            )
        ),
    )
    @pytest.mark.parametrize(
        "keys_expected,\
            status_code_expected, error",
        [
            (
                {
                    "id",
                    "fullname",
                    "shortname",
                    "startdate",
                    "enddate",
                    "timecreated",
                    "timemodified",
                },
                200,
                False,
            ),
        ],
    )
    def test_get_remote_courses(
        self, client_class, keys_expected, status_code_expected, error
    ):
        url = path_remote + path_courses
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))

        # Check that each course in the response contains the expected keys
        for course in response:
            assert keys_expected.issubset(course.keys())

    # Get Remote Content from LMS course
    @mock.patch(
        "requests.get",
        mock.Mock(
            side_effect=lambda k: (
                mock.Mock(
                    status_code=200,
                    json=lambda: [
                        {
                            "id": 76,
                            "name": "Erste Schritte",
                            "visible": 1,
                            "summary": "",
                            "summaryformat": 1,
                            "section": 0,
                            "hiddenbynumsections": 0,
                            "uservisible": True,
                            "modules": [
                                {
                                    "id": 513,
                                    "url": "ke.moodle.haski.app/feedback/view?id=513",
                                    "name": "Begriffserklärung HASKI (empfohlen)",
                                    "instance": 84,
                                    "contextid": 838,
                                    "visible": 1,
                                    "uservisible": True,
                                    "visibleoncoursepage": 1,
                                    "modicon": "ke.moodle.haski.app/?filtericon=1",
                                    "modname": "feedback",
                                    "modplural": "Feedback",
                                    "availability": None,
                                    "indent": 0,
                                    "onclick": "",
                                    "afterlink": None,
                                    "customdata": "",
                                    "noviewlink": False,
                                    "completion": 2,
                                    "completiondata": {
                                        "state": 0,
                                        "timecompleted": 0,
                                        "overrideby": None,
                                        "valueused": False,
                                        "hascompletion": True,
                                        "isautomatic": True,
                                        "istrackeduser": True,
                                        "uservisible": True,
                                        "details": [
                                            {
                                                "rulename": "completionsubmit",
                                                "rulevalue": {
                                                    "status": 0,
                                                    "description": "Submit feedback",
                                                },
                                            }
                                        ],
                                    },
                                    "downloadcontent": 1,
                                    "dates": [],
                                },
                                {
                                    "id": 601,
                                    "url": "ke.moodle.haski.app/h5pactivity/view?id601",
                                    "name": "Freiwilliges Emotionsbarometer",
                                    "instance": 384,
                                    "contextid": 926,
                                    "visible": 1,
                                    "uservisible": True,
                                    "visibleoncoursepage": 1,
                                    "modicon": "ke.moodle.haski.app/?filtericon=1",
                                    "modname": "h5pactivity",
                                    "modplural": "H5P",
                                    "availability": None,
                                    "indent": 0,
                                    "onclick": "",
                                    "afterlink": None,
                                    "customdata": '""',
                                    "noviewlink": False,
                                    "completion": 2,
                                    "completiondata": {
                                        "state": 1,
                                        "timecompleted": 1715080190,
                                        "overrideby": None,
                                        "valueused": False,
                                        "hascompletion": True,
                                        "isautomatic": True,
                                        "istrackeduser": True,
                                        "uservisible": True,
                                        "details": [
                                            {
                                                "rulename": "completionview",
                                                "rulevalue": {
                                                    "status": 1,
                                                    "description": "View",
                                                },
                                            }
                                        ],
                                    },
                                    "downloadcontent": 1,
                                    "dates": [],
                                },
                                {
                                    "id": 515,
                                    "url": "ke.moodle.haski.app/feedback/view?id=515",
                                    "name": "Freiwilliges Feedback vor dem Thema",
                                    "instance": 85,
                                    "contextid": 840,
                                    "visible": 1,
                                    "uservisible": True,
                                    "visibleoncoursepage": 1,
                                    "modicon": "ke.moodle.haski.app?filtericon=1",
                                    "modname": "feedback",
                                    "modplural": "Feedback",
                                    "availability": None,
                                    "indent": 0,
                                    "onclick": "",
                                    "afterlink": None,
                                    "customdata": "",
                                    "noviewlink": False,
                                    "completion": 2,
                                    "completiondata": {
                                        "state": 0,
                                        "timecompleted": 0,
                                        "overrideby": None,
                                        "valueused": False,
                                        "hascompletion": True,
                                        "isautomatic": True,
                                        "istrackeduser": True,
                                        "uservisible": True,
                                        "details": [
                                            {
                                                "rulename": "completionsubmit",
                                                "rulevalue": {
                                                    "status": 0,
                                                    "description": "Submit",
                                                },
                                            }
                                        ],
                                    },
                                    "downloadcontent": 1,
                                    "dates": [],
                                },
                                {
                                    "id": 514,
                                    "url": "ke.moodle.haski.app/h5pactivity/id=514",
                                    "name": "Freiwilliges Feedback zur intuitiven",
                                    "instance": 321,
                                    "contextid": 839,
                                    "visible": 1,
                                    "uservisible": True,
                                    "visibleoncoursepage": 1,
                                    "modicon": "ke.moodle.haski.app?filtericon=1",
                                    "modname": "h5pactivity",
                                    "modplural": "H5P",
                                    "availability": None,
                                    "indent": 0,
                                    "onclick": "",
                                    "afterlink": None,
                                    "customdata": '""',
                                    "noviewlink": False,
                                    "completion": 2,
                                    "completiondata": {
                                        "state": 1,
                                        "timecompleted": 1714373032,
                                        "overrideby": None,
                                        "valueused": False,
                                        "hascompletion": True,
                                        "isautomatic": True,
                                        "istrackeduser": True,
                                        "uservisible": True,
                                        "details": [
                                            {
                                                "rulename": "completionview",
                                                "rulevalue": {
                                                    "status": 1,
                                                    "description": "View",
                                                },
                                            }
                                        ],
                                    },
                                    "downloadcontent": 1,
                                    "dates": [],
                                },
                                {
                                    "id": 517,
                                    "url": "ke.moodle.haski.app/forum/view?id=517",
                                    "name": "Announcements",
                                    "instance": 9,
                                    "contextid": 842,
                                    "visible": 0,
                                    "uservisible": True,
                                    "visibleoncoursepage": 1,
                                    "modicon": "ke.moodle.haski.app/",
                                    "modname": "forum",
                                    "modplural": "Forums",
                                    "availability": None,
                                    "indent": 0,
                                    "onclick": "",
                                    "afterlink": None,
                                    "customdata": '""',
                                    "noviewlink": False,
                                    "completion": 0,
                                    "downloadcontent": 1,
                                    "dates": [],
                                },
                            ],
                        },
                    ],
                )
            )
        ),
    )
    @pytest.mark.parametrize(
        "expected_topic_keys, expected_learning_element_keys, expected_course_id,\
            status_code_expected, error",
        [
            (
                {"topic_lms_id", "topic_lms_name", "lms_learning_elements"},
                {"lms_activity_type", "lms_id", "lms_learning_element_name"},
                "1",
                200,
                False,
            ),
        ],
    )
    def test_get_remote_course_content(
        self,
        client_class,
        expected_topic_keys,
        expected_learning_element_keys,
        expected_course_id,
        status_code_expected,
        error,
    ):
        url = path_remote + path_course + "/" + expected_course_id + path_content
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        print(response)

        # Check that each topic in the response contains the expected keys
        for topic in response:
            assert expected_topic_keys.issubset(
                topic.keys()
            ), f"Missing keys in topic: {topic}"

        # Check that each learning element in the topic contains the expected keys
        for element in topic["lms_learning_elements"]:
            assert expected_learning_element_keys.issubset(
                element.keys()
            ), f"Missing keys in learning element: {element}"

    # Get User by ID
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (
                4,
                ["id", "name", "university", "lms_user_id", "role", "settings"],
                200,
                False,
            ),
            # User not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_get_user_by_id(
        self, client_class, lms_user_id, keys_expected, status_code_expected, error
    ):
        global user_id_student
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = path_user + "/" + str(user_id_use) + "/" + str(lms_user_id)
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get User Settings
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (4, ["theme", "pswd"], 200, False),
            # User not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_get_user_settings_by_id(
        self, client_class, lms_user_id, keys_expected, status_code_expected, error
    ):
        global user_id_student
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = (
            path_user + "/" + str(user_id_use) + "/" + str(lms_user_id) + path_settings
        )
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Get all learning element statuses for a student for a course
    @mock.patch(
        "requests.get",
        mock.Mock(
            side_effect=lambda k: (
                mock.Mock(
                    status_code=200,
                    json=lambda: {
                        "statuses": [
                            {"cmid": 1, "state": 0, "timecompleted": 0},
                            {"cmid": 2, "state": 0, "timecompleted": 0},
                        ]
                    },
                )
            )
        ),
    )
    @pytest.mark.parametrize(
        "course_id, student_id",
        [
            # Working Example
            (1, 1)
        ],
    )
    def test_get_activity_status_for_student(self, client_class, course_id, student_id):
        global user_id_student
        url = (
            path_lms_course
            + "/"
            + str(course_id)
            + path_student
            + "/"
            + str(student_id)
            + path_activity_status
        )
        r = client_class.get(url)
        assert r.status_code == 200
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        assert response == [
            {"cmid": 1, "state": 0, "timecompleted": 0},
            {"cmid": 2, "state": 0, "timecompleted": 0},
        ]

    # Get all learning element statuses for a student for a course
    @mock.patch(
        "requests.get",
        mock.Mock(
            side_effect=lambda k: (
                mock.Mock(
                    status_code=200,
                    json=lambda: {
                        "statuses": [
                            {"cmid": 1, "state": 0, "timecompleted": 0},
                            {"cmid": 2, "state": 0, "timecompleted": 0},
                        ]
                    },
                )
            )
        ),
    )
    @pytest.mark.parametrize(
        "course_id, student_id, \
                            learning_element_id",
        [
            # Working Example
            (1, 1, 2)
        ],
    )
    def test_get_activity_status_for_student_for_learning_element(
        self, client_class, course_id, student_id, learning_element_id
    ):
        global user_id_student
        url = (
            path_lms_course
            + "/"
            + str(course_id)
            + path_student
            + "/"
            + str(student_id)
            + "/"
            + "learningElementId/"
            + str(learning_element_id)
            + path_activity_status
        )
        r = client_class.get(url)
        assert r.status_code == 200
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        assert response == [{"cmid": 2, "state": 0, "timecompleted": 0}]

    # Get News with language and university
    @pytest.mark.parametrize(
        "language_id, university, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                "en",
                "TH-AB",
                [
                    "created_at",
                    "expiration_date",
                    "language_id",
                    "news_content",
                    "university",
                ],
                200,
            ),
            # No university
            (
                "en",
                None,
                [
                    "created_at",
                    "expiration_date",
                    "language_id",
                    "news_content",
                    "university",
                ],
                200,
            ),
        ],
    )
    def test_get_news(
        self, client_class, language_id, university, keys_expected, status_code_expected
    ):
        url = path_news + "/language/" + str(language_id) + "/university/"
        if university is not None:
            url = url + str(university)
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        assert "news" in response.keys()
        for key in keys_expected:
            for entry in response["news"]:
                assert key in entry.keys()

    # Get logbuffer entries for a user
    @pytest.mark.parametrize(
        "user_id, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                4,
                [
                    "user_id",
                    "content",
                    "date",
                ],
                200,
            ),
        ],
    )
    def test_get_logbuffer(
        self, client_class, user_id, keys_expected, status_code_expected
    ):
        url = path_user + "/" + str(user_id) + path_logbuffer
        r = client_class.get(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        assert "log" in response.keys()
        for key in keys_expected:
            for entry in response["log"]:
                assert key in entry.keys()

    # PUT METHODS
    # Update the settings of a User
    @pytest.mark.parametrize(
        "lms_user_id, request_body, \
                            keys_expected, status_code_expected, \
                            error",
        [
            # Working Example
            (4, {"theme": "dark", "pswd": "password"}, ["theme", "pswd"], 201, False),
            # User not found
            (
                1,
                {
                    "theme": [
                        {
                            "color": "dark",
                            "style": "dark",
                            "typography": "Comic Sans",
                            "language": "EN",
                        }
                    ],
                    "password": "password",
                },
                ["error", "message"],
                404,
                True,
            ),
        ],
    )
    def test_update_user_settings_by_id(
        self,
        client_class,
        lms_user_id,
        request_body,
        keys_expected,
        status_code_expected,
        error,
    ):
        global user_id_student
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = (
            path_user + "/" + str(user_id_use) + "/" + str(lms_user_id) + path_settings
        )
        r = client_class.put(url, json=request_body)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Update the learning style of a Student
    @pytest.mark.parametrize(
        "lms_user_id, request_body, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (
                4,
                {
                    "perception_dimension": "SNS",
                    "perception_value": 7,
                    "input_dimension": "VIS",
                    "input_value": 7,
                    "processing_dimension": "ACT",
                    "processing_value": 7,
                    "understanding_dimension": "GLO",
                    "understanding_value": 7,
                },
                [
                    "perception_dimension",
                    "perception_value",
                    "input_dimension",
                    "input_value",
                    "processing_dimension",
                    "processing_value",
                    "understanding_dimension",
                    "understanding_value",
                ],
                201,
                False,
            ),
            # User not found
            (
                1,
                {
                    "perception_dimension": "SNS",
                    "perception_value": 7,
                    "input_dimension": "VIS",
                    "input_value": 7,
                    "processing_dimension": "ACT",
                    "processing_value": 7,
                    "understanding_dimension": "GLO",
                    "understanding_value": 7,
                },
                ["error", "message"],
                404,
                True,
            ),
            # Empty Request body
            (4, {}, ["error", "message"], 400, False),
            # Wrong numbers in request body
            (
                4,
                {
                    "perception_dimension": "SNS",
                    "perception_value": 12,
                    "input_dimension": "VIS",
                    "input_value": 7,
                    "processing_dimension": "ACT",
                    "processing_value": 7,
                    "understanding_dimension": "GLO",
                    "understanding_value": 7,
                },
                ["error", "message"],
                400,
                False,
            ),
            # Wrong number of dimensions in request body
            (
                4,
                {
                    "perception_dimension": "SNS",
                    "perception_value": 7,
                    "input_dimension": "VIS",
                    "input_value": 7,
                    "processing_dimension": "ACT",
                    "processing_value": 7,
                },
                ["error", "message"],
                400,
                False,
            ),
        ],
    )
    def test_update_learning_style_by_student_id(
        self,
        client_class,
        lms_user_id,
        request_body,
        keys_expected,
        status_code_expected,
        error,
    ):
        global user_id_student, student_id
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id)
            + path_learning_style
        )
        r = client_class.put(url, json=request_body)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Update User data from Moodle
    @pytest.mark.parametrize(
        "input, moodle_user_id, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                {
                    "name": "Max Mustermann",
                    "role": "Student",
                    "university": "TH-AB",
                    "settings": [
                        {
                            "theme": [
                                {
                                    "color": "dark",
                                    "style": "dark",
                                    "typography": "Arial Black",
                                    "language": "DE",
                                }
                            ],
                            "password": "password",
                        }
                    ],
                },
                4,
                ["id", "name", "university", "lms_user_id", "role", "settings"],
                201,
            ),
            # Missing Parameter
            (
                {
                    "role": "Student",
                    "university": "TH-AB",
                    "settings": [
                        {
                            "theme": [
                                {
                                    "color": "dark",
                                    "style": "dark",
                                    "typography": "Arial Black",
                                    "language": "DE",
                                }
                            ],
                            "password": "password",
                        }
                    ],
                },
                4,
                ["error", "message"],
                400,
            ),
        ],
    )
    def test_update_user_from_moodle(
        self, client_class, input, moodle_user_id, keys_expected, status_code_expected
    ):
        global user_id_student
        url = path_lms_user + "/" + str(user_id_student) + "/" + str(moodle_user_id)
        r = client_class.put(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Update Course data from Moodle
    @pytest.mark.parametrize(
        "input, moodle_course_id, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                {
                    "name": "Test Course Updated",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "start_date": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                },
                1,
                ["id", "name", "lms_id", "created_at", "created_by", "university"],
                201,
            ),
            # Missing Parameter
            (
                {
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                },
                1,
                ["error", "message"],
                400,
            ),
            # Parameter with wrong data type
            (
                {
                    "name": "Test Course Updated",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "01.01.2023",
                    "university": "TH-AB",
                },
                1,
                ["error", "message"],
                400,
            ),
        ],
    )
    def test_update_course_from_moodle(
        self, client_class, input, moodle_course_id, keys_expected, status_code_expected
    ):
        global course_id
        url = path_lms_course + "/" + str(course_id) + "/" + str(moodle_course_id)
        r = client_class.put(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    @pytest.mark.parametrize(
        "input, moodle_course_id, keys_expected,\
                            status_code_expected",
        [
            # Working Example
            (
                {
                    "name": "Test Course Updated",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                    "start_date": "2023-08-01T13:37:42Z",
                },
                1,
                [
                    "id",
                    "name",
                    "lms_id",
                    "created_at",
                    "created_by",
                    "university",
                    "start_date",
                ],
                201,
            ),
            # Missing Parameter
            (
                {
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                    "start_date": "2023-08-01T13:37:42Z",
                },
                1,
                ["error", "message"],
                400,
            ),
            # Parameter with wrong data type
            (
                {
                    "name": "Test Course Updated",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                    "start_date": "what is this?",
                },
                1,
                ["error", "message"],
                400,
            ),
        ],
    )
    def test_update_course_from_moodle_with_start_date(
        self, client_class, input, moodle_course_id, keys_expected, status_code_expected
    ):
        global course_id
        url = path_lms_course + "/" + str(course_id) + "/" + str(moodle_course_id)
        r = client_class.put(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Update a Topic from Moodle
    @pytest.mark.parametrize(
        "input, moodle_course_id, moodle_topic_id,\
                            keys_expected, status_code_expected, sub_topic",
        [
            # Working Example for Topic
            (
                {
                    "name": "Test Topic Updated",
                    "is_topic": True,
                    "parent_id": None,
                    "contains_le": False,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                },
                1,
                1,
                [
                    "id",
                    "name",
                    "lms_id",
                    "is_topic",
                    "parent_id",
                    "contains_le",
                    "created_by",
                    "created_at",
                    "university",
                ],
                201,
                False,
            ),
            # Working Example for Sub-Topic
            (
                {
                    "name": "Test Sub-Topic Updated",
                    "is_topic": False,
                    "parent_id": None,
                    "contains_le": True,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                },
                1,
                1,
                [
                    "id",
                    "name",
                    "lms_id",
                    "is_topic",
                    "parent_id",
                    "contains_le",
                    "created_by",
                    "created_at",
                    "university",
                ],
                201,
                True,
            ),
            # Missing Parameter
            (
                {
                    "is_topic": True,
                    "parent_id": 1,
                    "contains_le": False,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                },
                1,
                1,
                ["error", "message"],
                400,
                False,
            ),
            # Parameter with wrong data type
            (
                {
                    "name": "Test Topic Updated",
                    "is_topic": True,
                    "parent_id": None,
                    "contains_le": False,
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "01-01-2023",
                    "university": "TH-AB",
                },
                1,
                1,
                ["error", "message"],
                400,
                False,
            ),
        ],
    )
    def test_update_topic_from_moodle(
        self,
        client_class,
        input,
        moodle_course_id,
        moodle_topic_id,
        keys_expected,
        status_code_expected,
        sub_topic,
    ):
        global course_id, topic_id, sub_topic_id
        if sub_topic:
            topic_id_use = sub_topic_id
            input["parent_id"] = topic_id
        else:
            topic_id_use = topic_id
        url = path_lms_topic + "/" + str(topic_id_use) + "/" + str(moodle_topic_id)
        r = client_class.put(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Update an Learning Element from Moodle
    @pytest.mark.parametrize(
        "input, moodle_course_id, moodle_topic_id,\
                            moodle_learning_element_id, keys_expected,\
                            status_code_expected",
        [
            # Working Example for LE
            (
                {
                    "activity_type": "Quiz",
                    "classification": "RQ",
                    "name": "Test Learning Element Updated",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                },
                1,
                1,
                1,
                [
                    "id",
                    "lms_id",
                    "activity_type",
                    "classification",
                    "name",
                    "created_by",
                    "created_at",
                    "university",
                ],
                201,
            ),
            # Missing Parameter
            (
                {
                    "classification": "RQ",
                    "name": "Test Learning Element Updated",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "2018-07-21T17:32:28Z",
                    "university": "TH-AB",
                },
                1,
                1,
                1,
                ["error", "message"],
                400,
            ),
            # Parameter with wrong data type
            (
                {
                    "activity_type": "Quiz",
                    "classification": "RQ",
                    "name": "Test Learning Element Updated",
                    "created_by": "Maria Musterfrau",
                    "created_at": "2023-08-01T13:37:42Z",
                    "last_updated": "01.01.2023",
                    "university": "TH-AB",
                },
                1,
                1,
                1,
                ["error", "message"],
                400,
            ),
        ],
    )
    def test_update_le_from_moodle(
        self,
        client_class,
        input,
        moodle_course_id,
        moodle_topic_id,
        moodle_learning_element_id,
        keys_expected,
        status_code_expected,
    ):
        global course_id, sub_topic_id, learning_element_id
        url = (
            path_lms_learning_element
            + "/"
            + str(learning_element_id)
            + "/"
            + str(moodle_learning_element_id)
        )
        r = client_class.put(url, json=input)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    @pytest.mark.parametrize(
        "keys_expected, status_code_expected, save_id",
        [
            # Working Example
            (
                ["CREATED", "course_id", "students_added"],
                201,
                True,
            ),
        ],
    )
    def test_api_add_all_students_to_course(
        self, client_class, keys_expected, status_code_expected, save_id
    ):
        url = path_course + "/" + str("1") + "/allStudents"
        r = client_class.post(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    @pytest.mark.parametrize(
        "keys_expected, status_code_expected, save_id",
        [
            # Working Example
            (
                ["CREATED", "course_id", "students_added"],
                201,
                True,
            ),
        ],
    )
    def test_api_add_all_students_to_topics(
        self, client_class, keys_expected, status_code_expected, save_id
    ):
        global course_id
        course_id_use = course_id
        url = path_course + "/" + str(course_id_use) + "/topics" + "/allStudents"
        r = client_class.post(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # DELETE METHODS
    # Reset User Settings
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (4, ["theme", "pswd"], 200, False),
            # User not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_reset_user_settings(
        self, client_class, lms_user_id, keys_expected, status_code_expected, error
    ):
        global user_id_student
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = (
            path_user + "/" + str(user_id_use) + "/" + str(lms_user_id) + path_settings
        )
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Reset Learning Characteristics
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (
                4,
                [
                    "id",
                    "knowledge",
                    "learning_analytics",
                    "learning_strategy",
                    "learning_style",
                    "student_id",
                ],
                200,
                False,
            ),
            # User not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_reset_learning_characteristics(
        self, client_class, lms_user_id, keys_expected, status_code_expected, error
    ):
        global user_id_student, student_id
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id)
            + path_learning_characteristics
        )
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in keys_expected:
            assert key in response.keys()

    # Reset Learning Analytics
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (4, ["id", "characteristic_id"], 200, False),
            # User not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_reset_learning_analytics(
        self, client_class, lms_user_id, keys_expected, status_code_expected, error
    ):
        global user_id_student, student_id
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id)
            + path_learning_analytics
        )
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    # Reset Learning Style
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (
                4,
                [
                    "id",
                    "characteristic_id",
                    "perception_dimension",
                    "perception_value",
                    "input_dimension",
                    "input_value",
                    "processing_dimension",
                    "processing_value",
                    "understanding_dimension",
                    "understanding_value",
                ],
                200,
                False,
            ),
            # User not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_reset_learning_style(
        self, client_class, lms_user_id, keys_expected, status_code_expected, error
    ):
        global user_id_student, student_id
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id)
            + path_learning_style
        )
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    # Reset Learning Strategy
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (
                4,
                [
                    "att",
                    "characteristic_id",
                    "cogn_str",
                    "con",
                    "crit_rev",
                    "eff",
                    "elab",
                    "ext_res_mng_str",
                    "goal_plan",
                    "id",
                    "int_res_mng_str",
                    "lit_res",
                    "lrn_env",
                    "lrn_w_cls",
                    "metacogn_str",
                    "org",
                    "reg",
                    "rep",
                    "time",
                ],
                200,
                False,
            ),
            # User not found
            (100, ["error", "message"], 404, True),
        ],
    )
    def test_reset_learning_strategy(
        self, client_class, lms_user_id, keys_expected, status_code_expected, error
    ):
        global user_id_student, student_id
        if error:
            user_id_use = 99999
            student_id_use = 99999
        else:
            user_id_use = user_id_student
            student_id_use = student_id
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id_use)
            + path_learning_strategy
        )
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    # Reset Knowledge
    @pytest.mark.parametrize(
        "lms_user_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (4, ["id", "characteristic_id"], 200, False),
            # User not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_reset_knowledge(
        self, client_class, lms_user_id, keys_expected, status_code_expected, error
    ):
        global user_id_student, student_id
        if error:
            user_id_use = 99999
        else:
            user_id_use = user_id_student
        url = (
            path_user
            + "/"
            + str(user_id_use)
            + "/"
            + str(lms_user_id)
            + path_student
            + "/"
            + str(student_id)
            + path_knowledge
        )
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    # Delete a Contact Form
    @pytest.mark.parametrize(
        "lms_user_id, user_id,\
                            status_code_expected",
        [
            # Working Example
            (4, 4, 201)
        ],
    )
    def test_delete_contact_form(
        self, client_class, lms_user_id, user_id, status_code_expected
    ):
        user_id_student = user_id
        url = (
            path_user
            + "/"
            + str(user_id_student)
            + "/"
            + str(lms_user_id)
            + path_contactform
        )
        r = client_class.delete(url)
        assert r.status_code == status_code_expected

    # Delete User
    @pytest.mark.parametrize(
        "moodle_user_id, keys_expected,\
                            status_code_expected, student",
        [
            # Working Example Student
            (4, ["message"], 200, True),
            # Working Example Teacher
            (3, ["message"], 200, False),
            # User not found
            (4, ["error", "message"], 404, True),
        ],
    )
    def test_delete_user(
        self, client_class, moodle_user_id, keys_expected, status_code_expected, student
    ):
        global user_id_student, user_id_teacher
        if student:
            user_id_use = user_id_student
        else:
            user_id_use = user_id_teacher
        url = path_lms_user + "/" + str(user_id_use) + "/" + str(moodle_user_id)
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    # Delete Learning Element
    @pytest.mark.parametrize(
        "moodle_course_id, moodle_topic_id,\
                            moodle_learning_element_id, keys_expected,\
                            status_code_expected, error_course,\
                            error_topic, error_le",
        [
            # Working Example
            (1, 1, 1, ["message"], 200, False, False, False),
            # Course not found
            (1, 1, 1, ["error", "message"], 404, True, False, False),
            # Topic not found
            (1, 1, 1, ["error", "message"], 404, False, True, False),
            # Learning Element not found
            (1, 1, 1, ["error", "message"], 404, False, False, True),
        ],
    )
    def test_api_delete_le_from_moodle(
        self,
        client_class,
        moodle_course_id,
        moodle_topic_id,
        moodle_learning_element_id,
        keys_expected,
        status_code_expected,
        error_course,
        error_topic,
        error_le,
    ):
        global course_id, sub_topic_id, learning_element_id
        if error_le:
            learning_element_id_use = 99999
        else:
            learning_element_id_use = learning_element_id
        url = (
            path_lms_learning_element
            + "/"
            + str(learning_element_id_use)
            + "/"
            + str(moodle_learning_element_id)
        )
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    # Delete Topic
    @pytest.mark.parametrize(
        "moodle_course_id, moodle_topic_id,\
                            keys_expected, status_code_expected,\
                            error_course, error_topic",
        [
            # Working Example
            (1, 1, ["message"], 200, False, False),
            # Course not found
            (1, 1, ["error", "message"], 404, True, False),
            # Topic not found
            (1, 1, ["error", "message"], 404, False, True),
        ],
    )
    def test_api_delete_topic_from_moodle(
        self,
        client_class,
        moodle_course_id,
        moodle_topic_id,
        keys_expected,
        status_code_expected,
        error_course,
        error_topic,
    ):
        global course_id, sub_topic_id
        if error_topic:
            topic_id_use = 99999
        else:
            topic_id_use = sub_topic_id
        url = path_lms_topic + "/" + str(topic_id_use) + "/" + str(moodle_topic_id)
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

    # Delete Course
    @pytest.mark.parametrize(
        "moodle_course_id, keys_expected,\
                            status_code_expected, error",
        [
            # Working Example
            (1, ["message"], 200, False),
            # Course not found
            (1, ["error", "message"], 404, True),
        ],
    )
    def test_api_delete_course_from_moodle(
        self, client_class, moodle_course_id, keys_expected, status_code_expected, error
    ):
        global course_id
        if error:
            course_id_use = 99999
        else:
            course_id_use = course_id
        url = path_lms_course + "/" + str(course_id_use) + "/" + str(moodle_course_id)
        r = client_class.delete(url)
        assert r.status_code == status_code_expected
        response = json.loads(r.data.decode("utf-8").strip("\n"))
        for key in response.keys():
            assert key in keys_expected

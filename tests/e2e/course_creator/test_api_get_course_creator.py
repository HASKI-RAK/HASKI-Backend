# Tests for get methods
import pytest
import json


@pytest.mark.parametrize("user_id, lms_user_id, course_creator_id,\
                         keys_expected_1, keys_expected_2, \
                         status_code_expected", [
    # Working Example
    (
        1,
        1,
        1,
        ['courses'],
        ['id', 'name', 'lms_id', 'created_at', 'nr_teachers', 'teachers'],
        200
    ),
    # User not found
    (
        2,
        1,
        1,
        ['error'],
        [],
        404
    )
])
def test_api_get_courses_by_course_creator_id(
    client,
    user_id,
    lms_user_id,
    course_creator_id,
    keys_expected_1,
    keys_expected_2,
    status_code_expected
):
    url = "/user/" + str(user_id) + "/" + str(lms_user_id) + \
        "/courseCreator/" + str(course_creator_id) + "/course"
    r = client.get(url)
    assert r.status_code == status_code_expected
    response = json.loads(r.data.decode("utf-8").strip('\n'))
    if 'courses' in keys_expected_1:
        for key in response['courses'].keys():
            assert key in keys_expected_2
    else:
        for key in response.keys():
            assert key in keys_expected_1
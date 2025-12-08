import unittest

from service_layer.lti.Roles import RoleMapper, lti_permissions, lti_roles
from utils.auth.permissions import Permissions
from utils.constants import (
    role_admin_string,
    role_course_creator_string,
    role_student_string,
)


class TestRoles(unittest.TestCase):
    def test_lti_roles(self):
        """[HASKI-REQ-0028] Test if lti_roles has the expected mappings."""
        expected_roles = {
            "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor": role_course_creator_string,  # noqa: E501
            "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner": role_student_string,  # noqa: E501
            "http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator": role_admin_string,  # noqa: E501
        }
        self.assertDictEqual(lti_roles, expected_roles)

    def test_lti_permissions(self):
        """[HASKI-REQ-0028] Test if lti_permissions has the expected mappings."""
        expected_permissions = {
            role_course_creator_string: [Permissions.READ, Permissions.WRITE],
            role_student_string: [Permissions.READ],
            role_admin_string: [Permissions.READ, Permissions.WRITE, Permissions.ADMIN],
        }
        self.assertDictEqual(lti_permissions, expected_permissions)


class TestRoleMapper(unittest.TestCase):
    def test_map_role(self):
        """[HASKI-REQ-0028] Test the map_role method."""
        self.assertEqual(
            RoleMapper.map_role(
                "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"
            ),
            role_course_creator_string,
        )
        self.assertEqual(RoleMapper.map_role("unknown_role"), "Unknown")

    def test_constructor(self):
        """[HASKI-REQ-0028] Test the __init__ method."""
        role_mapper = RoleMapper(
            [
                "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner",
                "unknown_role",
            ]
        )
        self.assertEqual(role_mapper.get_role(), role_student_string)
        role_mapper = RoleMapper(["unknown_role"])
        self.assertEqual(role_mapper.get_role(), "Unknown")

    def test_get_role(self):
        """[HASKI-REQ-0028] Test the get_role method."""
        role_mapper = RoleMapper(
            ["http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator"]
        )
        self.assertEqual(role_mapper.get_role(), role_admin_string)

    def test_get_permissions(self):
        """[HASKI-REQ-0028] Test the get_permissions method."""
        role_mapper = RoleMapper(
            ["http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor"]
        )
        self.assertEqual(role_mapper.get_role(), role_course_creator_string)
        self.assertEqual(
            role_mapper.get_permissions(), [Permissions.READ, Permissions.WRITE]
        )  # Replace with actual Permissions enum


if __name__ == "__main__":
    unittest.main()

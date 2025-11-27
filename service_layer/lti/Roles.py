from utils.auth.permissions import Permissions
from utils.constants import (
    role_admin_string,
    role_course_creator_string,
    role_student_string,
)

# This file contains the mapping of IMS roles to LTI / LMS roles
# Moodle Manager & Teacher: Instructor
# Moodle Admin: Administrator
# Moodle Student: Learner
lti_roles = {
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor": role_course_creator_string,  # noqa: E501
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner": role_student_string,  # noqa: E501
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator": role_admin_string,  # noqa: E501
}

lti_permissions = {
    role_course_creator_string: [Permissions.READ, Permissions.WRITE],
    role_student_string: [Permissions.READ],
    role_admin_string: [Permissions.READ, Permissions.WRITE, Permissions.ADMIN],
}


class RoleMapper:
    """Maps IMS roles to a single LTI role
    Example:
    IMS roles:
    http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor,\
        http://purl.imsglobal.org/vocab/lis/v2/membership#Learner
    LTI role: Instructor
    return by get_role(): course creator
    """

    # map IMS roles to LTI roles
    @staticmethod
    def map_role(role: str):
        if role in lti_roles:
            return lti_roles[role]
        return "Unknown"

    def __init__(self, roles_list: list[str]):
        self.role: str = "Unknown"
        for role in roles_list:
            if RoleMapper.map_role(role) != "Unknown":
                self.role = RoleMapper.map_role(role)
                break

    def get_role(self):
        return self.role

    def get_permissions(self) -> list[Permissions]:
        return lti_permissions[self.role]

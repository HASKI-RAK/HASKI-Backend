from utils.auth.permissions import Permissions

# This file contains the mapping of IMS roles to LTI / LMS roles
# Moodle Manager, Teacher: Instructor, Moodle Admin: Administrator, Moodle Student: Learner
lti_roles = {
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor": "course creator",
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Learner": "student",
    "http://purl.imsglobal.org/vocab/lis/v2/membership#Administrator": "admin",
}

lti_permissions = {
    "course creator": [Permissions.READ, Permissions.WRITE],
    "student": [Permissions.READ],
    "admin": [Permissions.READ, Permissions.WRITE, Permissions.ADMIN],
}


class RoleMapper:
    """Maps IMS roles to a single LTI role
    Example:
    IMS roles: http://purl.imsglobal.org/vocab/lis/v2/membership#Instructor,\
        http://purl.imsglobal.org/vocab/lis/v2/membership#Learner
    LTI role: tutor
    return by get_role(): tutor
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

from abc import ABC, abstractmethod

from service_layer.lti.lms.Platform import Platform


class OIDCLogin(ABC):
    """Base class for OIDC login. Derive from\
        this class and implement the abstract methods"""

    _platform: Platform

    def __init__(self, request):
        self._request = request

    @abstractmethod
    def check_params(self) -> "OIDCLogin":
        pass

    @abstractmethod
    def auth_redirect(self):
        pass

    @abstractmethod
    def lti_launch_from_id_token(self):
        pass

    @abstractmethod
    def verify_id_token(self) -> "OIDCLogin":
        pass

    @abstractmethod
    def get_cookie_expiration(self):
        pass

    @abstractmethod
    def get_logout(self):
        pass

    @staticmethod
    def make_url_accept_param(url):
        if "?" in url:
            return url + "&"
        else:
            return url + "?"

from functools import wraps

from flask import request

import errors.errors as err
import service_layer.crypto.JWTKeyManagement as JWTKeyManagement
from utils.auth.permissions import Permissions


def authorize(required_permissions: list[Permissions]):
    """🔑 Decorator for checking if user has the required \
        permission to access the endpoint.
        Example usage:
        @app.route('/api/endpoint')
        @authorize([Permissions.READ, Permissions.WRITE])
        def endpoint():"""

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kws):
            state_jwt = request.cookies.get("haski_state")
            if state_jwt is None:
                raise err.StateNotMatchingError()

            state = JWTKeyManagement.verify_jwt(state_jwt)
            if not JWTKeyManagement.verify_jwt_payload(state, verify_nonce=False):
                raise err.UnauthorizedError()

            # Check if user has any of the required permissions
            user_permissions: list[str] = state.get("permissions", [])
            if not all(
                permission.value in user_permissions
                for permission in required_permissions
            ):
                raise err.UnauthorizedError(
                    message="You do not have the necessary\
                        permissions to perform this action",
                    status_code=401,
                )

            return f(state, *args, **kws)

        return decorated_function

    return decorator

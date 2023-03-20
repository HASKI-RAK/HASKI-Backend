"""This module provides a simple storage for LTI launch data. It is used to store the launch data for the LTI launch request with short lived keys. The keys are used to retrieve the launch data. The launch data is stored for 1 minute. After that the key is deleted and the launch data is no longer available."""
from datetime import datetime, timedelta
from typing import Dict

_dict : Dict[str, tuple[str, datetime]] = {}
def set_value(key, value):
    """ Sets the state value for a given key. If the key already exists, it will throw an exception.
    This is used for later retrieval and confirmation of the state.
    """
    # if conflict throw exception
    if key in _dict:
        raise KeyError("Key already exists")
    _dict[key] = (value, datetime.now() + timedelta(minutes=1)) # 1 minute expiration for authorization

def get_value(key) -> str | None:
    if key in _dict:
        value, expiration = _dict[key]
        if expiration < datetime.now():
            del _dict[key]
            return None
        return value
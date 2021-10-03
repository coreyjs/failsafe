__version__ = '0.1.0'

from failsafe.client import Client
from failsafe.exceptions import AuthenticationError


def service(api_key: str):
    if api_key is None:
        raise AuthenticationError("Missing api_key")

    return Client(api_key=api_key)




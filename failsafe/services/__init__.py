
import requests
from enum import Enum

from failsafe.exceptions import ServerError
from failsafe.session import Session


class HttpMethod(Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4



class BaseService:

    def __init__(self, session: Session):
        self.session = session
        self.api_root = 'https://www.bungie.net/Platform/'

    def _headers(self):
        return {
            'X-API-Key': self.session.api_key,
            'Content-Type': 'application/json'
        }

    def call(self, url: str, method: HttpMethod = HttpMethod.GET, additional_headers: {} = {}):
        headers = {**self._headers(), **additional_headers}

        req = None
        if method == HttpMethod.GET:
            req = requests.get(url=url, headers=headers)
        elif method == HttpMethod.POST:
            pass

        if req.status_code == requests.codes.internal_server_error:
            raise ServerError('Error returned from Bungie API')

class ApiError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class AuthenticationError(ApiError):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class ServerError(ApiError):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

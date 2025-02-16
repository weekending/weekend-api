from .http import BaseStatus


class APIException(Exception):
    def __init__(self, http: BaseStatus, **kwargs):
        super().__init__(http.message)
        self.http = http
        self.extra = kwargs

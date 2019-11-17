from flask import jsonify


class HttpErrorBaseException(Exception):
    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv

    def to_json_response(self):
        response = jsonify(self.to_dict())
        response.status_code = self.status_code
        return response


class BadRequest(HttpErrorBaseException):
    def __init__(self, message, payload=None):
        HttpErrorBaseException.__init__(self, message, 400, payload)

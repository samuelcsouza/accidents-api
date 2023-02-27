
class Error(Exception):
    status_code: int
    error: dict


class NotFound(Error):
    status_code = 404

    error = {
        "type": "not found",
        "description": "The server can not find the requested resource.",
    }


class RouteNotFound(Error):
    status_code = 404

    error = {
        "type": "resource not found",
        "description": "The requested resource does not exists."
    }

class ErrorAuthenticationInvalid(Error):
    status_code = 401

    error = {
        "type": "invalid_authentication",
        "description": "The authentication key provided is invalid."
    }

class Forbidden:
    status_code = 403

    error = {
        "type": "forbidden",
        "description": "The client does not have " +
                       "access rights to the content.",
    }

class ErrorInternal:
    status_code = 500

    error = {
        "type": "internal_error",
        "description": "An internal error has occurred " +
                       "while processing the request.",
    }

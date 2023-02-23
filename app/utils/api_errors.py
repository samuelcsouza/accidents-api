
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


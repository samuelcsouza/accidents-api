from utils.api_errors import Error, RouteNotFound, ErrorInternal
from socketify import Request, Response


def raise_error_response(res: Response, req: Request, error: Error) -> None:
    res.write_status(error.status_code).end(error.error)

def raise_error_route_not_found(res: Response, req: Request) -> Exception:
    raise RouteNotFound

def error_handler(error: Exception, res: Response, req: Request) -> None:
    if isinstance(error, Error):
        res.write_status(error.status_code).end(error.error)
        return False
    print(str(error))
    res.write_status(ErrorInternal.status_code).end(ErrorInternal.error)
from socketify import Request, Response
from socketify_app import app, router
from database import get_database
from utils.api_errors import NotFound

@router.get("/")
def list_accidents(res: Response, req: Request):
    _db = get_database()["accidents"]
    _query = {}
    _columns_to_exclude = {"_id": False, "location": False}

    docs = _db.find(_query, _columns_to_exclude).limit(10)

    res.end(list(docs))


@router.get("/:id")
def get_by_id(res: Response, req: Request):
    _db = get_database()["accidents"]

    paramter_id = req.get_parameter(0)

    _query = {"id": paramter_id}
    _columns_to_exclude = {"_id": False, "location": False}

    docs = _db.find_one(_query, _columns_to_exclude)

    if not docs:
        raise NotFound

    res.end(docs)


@router.get("/city/:city")
def get_by_city(res: Response, req: Request):
    _db = get_database()["accidents"]

    parameter_city = req.get_parameter(0)

    _query = {"municipio": parameter_city.upper()}
    _columns_to_exclude = {"_id": False, "location": False}

    docs = _db.find(_query, _columns_to_exclude)

    if not docs:
        raise NotFound

    res.end(list(docs))


@router.get("/state/:state")
def get_by_state(res: Response, req: Request):
    _db = get_database()["accidents"]

    parameter_city = req.get_parameter(0)

    _query = {"uf": parameter_city.upper()}
    _columns_to_exclude = {"_id": False, "location": False}

    docs = _db.find(_query, _columns_to_exclude)

    if not docs:
        raise NotFound

    res.end(list(docs))

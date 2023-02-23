from pymongo import MongoClient
from pymongo.database import Database
from config.settings import get_settings

_mongo = None


def get_mongo():
    global _mongo
    if not _mongo:
        _mongo = MongoClient(get_settings().MONGO_URI, connect=False)
    return _mongo


def get_database() -> Database:
    _mongo = get_mongo()
    return _mongo[get_settings().MONGO_DATABASE]


def close_connection():
    get_mongo().close()
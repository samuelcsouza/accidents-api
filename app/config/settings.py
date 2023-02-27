import os
import json
from dotenv import load_dotenv
from pydantic import BaseSettings
from typing import Dict
from urllib.request import urlopen

load_dotenv()


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"

    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")

    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")
    JWT_AUDIENCE: str = os.getenv("JWT_AUDIENCE")
    JWT_RSA_KEY: Dict = json.loads(
        urlopen(os.getenv('JWT_URL_RSA_KEY')).read())
    JWT_ISSUER: str = os.getenv("JWT_ISSUER")

def get_settings() -> Settings:
    return Settings()

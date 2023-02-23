import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"

    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_DATABASE: str = os.getenv("MONGO_DATABASE")

def get_settings() -> Settings:
    return Settings()

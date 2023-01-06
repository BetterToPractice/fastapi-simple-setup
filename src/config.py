import os

from dotenv import load_dotenv
from pydantic import BaseSettings


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


class Settings(BaseSettings):
    testing: bool = True
    database_url: str = "postgresql+psycopg2://postgres:postgres@localhost:5432"


settings = Settings()

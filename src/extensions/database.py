import os

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from src import settings

engine = create_engine(settings.settings.database_url)
Base = declarative_base()

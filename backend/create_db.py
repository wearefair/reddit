import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database

from reddit.models import Base

db_url=os.environ['SQLALCHEMY_DB_URL']

engine = create_engine(db_url)
if not database_exists(engine.url):
    create_database(engine.url)
Base.metadata.bind = engine
Base.metadata.drop_all()
Base.metadata.create_all()

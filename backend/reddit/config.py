import os

class Config(object):
    ENV = os.environ.get('ENV', 'dev')
    SQLALCHEMY_DB_URL = os.environ.get('SQLALCHEMY_DB_URL', '')

import os


class Config(object):
    ENV = os.environ.get('ENV', 'dev')
    DATABASE_URL = os.environ.get('DATABASE_URL', '')

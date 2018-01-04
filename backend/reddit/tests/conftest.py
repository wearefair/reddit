import pytest

from sqlalchemy.engine import create_engine
from sqlalchemy.orm.session import Session

from reddit.config import Config
from reddit.server import create_app
from reddit.models import *  # noqa
from reddit.models import Base


@pytest.fixture(scope='session')
def engine(request):
    """Session-wide `Flask` application"""
    engine = create_engine(Config.DATABASE_URL)

    connection = engine.connect()
    Base.metadata.drop_all(connection)  # Clean up any leftover db
    Base.metadata.create_all(connection)

    def teardown():
        engine.dispose()
        engine2 = create_engine(Config.DATABASE_URL)
        connection = engine2.connect()
        Base.metadata.drop_all(connection)  # Clean up any leftover db
        connection.close()
        engine2.dispose()

    request.addfinalizer(teardown)
    return engine


@pytest.fixture(scope='session')
def connection(engine, request):
    """Session-wide `Flask` application"""
    connection = engine.connect()

    def teardown():
        connection.close()

    request.addfinalizer(teardown)
    return connection


@pytest.fixture(scope='function')
def db(mocker, connection, reddit, app, request):
    """Creates a new database session for a test."""
    tx = connection.begin()
    session = Session(connection)
    reddit.db_session = session
    reddit.database.session = session

    def teardown():
        if tx.is_active:
            tx.rollback()

    request.addfinalizer(teardown)
    if request.cls:
        request.cls.db = session
        request.cls.reddit = reddit
        request.cls.app = app

    return session


@pytest.fixture(scope='session')
def reddit(engine, connection, request):
    """Session-wide `Flask` application"""
    app = create_app()
    app.init()
    app.database.close()
    app.database.engine.dispose()
    app.database.engine = engine

    ctx = app.app_context()
    ctx.push()

    def teardown():
        ctx.pop()

    request.addfinalizer(teardown)
    return app


@pytest.fixture(scope='session')
def app(reddit, request):
    """Session-wide `Flask` application"""
    return reddit.test_client()
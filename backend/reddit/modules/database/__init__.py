from reddit.modules.database.database import Database
from reddit.config import Config


def initialize(app):
    """
    Provides the database session on the application object.
    """
    app.database = Database(connection_url=Config.DATABASE_URL,
                            environment=Config.ENV, pool_size=1)
    app.db_session = app.database.session

    if Config.ENV != 'test':
        @app.teardown_appcontext
        def shutdown_session(exception=None):
            """Clean up the database on shutdown"""
            app.db_session.remove()


__all__ = [
    'initialize',
    'Database'
]

from sqlalchemy import create_engine
from sqlalchemy.engine import reflection
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
)
from sqlalchemy.schema import (
    DropConstraint,
    DropTable,
    ForeignKeyConstraint,
    MetaData,
    Table,
)

from reddit.models import Base


class Database(object):
    """Minimal wrapper around the SQLAlchemy database"""

    def __init__(self, connection_url=None, logger=None, environment=None,
                 pool_size=5):
        """
        :param logger: Logger to use, if `None` nothing will be logged.
        :type logger: Python standard logger object, see `logging` module
        """
        if environment is None:
            environment = 'development'

        self.engine = create_engine(connection_url,
                                    convert_unicode=True,
                                    pool_size=pool_size)

        self.session = scoped_session(sessionmaker(autocommit=False,
                                                   autoflush=False,
                                                   bind=self.engine))
        self._logger = logger
        self._env = environment

    def init(self):
        """
        Creates the schema, or resets the schema if running in a test
        environment.
        """
        self.reset()

    def _nuke_db(self):
        self._log('Nuking the database...')

        inspector = reflection.Inspector.from_engine(self.engine)
        # gather all data first before dropping anything.
        # some DBs lock after things have been dropped in
        # a transaction.
        metadata = MetaData()

        tbs = []
        all_fks = []

        for table_name in inspector.get_table_names():
            fks = []
            for fk in inspector.get_foreign_keys(table_name):
                if not fk['name']:
                    continue
                fks.append(
                    ForeignKeyConstraint((), (), name=fk['name'])
                )
            t = Table(table_name, metadata, *fks)
            tbs.append(t)
            all_fks.extend(fks)

        for fkc in all_fks:
            self.session.execute(DropConstraint(fkc))

        for table in tbs:
            self.session.execute(DropTable(table))

        self.session.commit()

    def reset(self):
        """Drops all tables and recreates the schema"""
        self._log("Resetting database...")
        self._nuke_db()
        self.create()

    def create(self):
        """Creates the Schema and required fixtures"""
        Base.metadata.create_all(bind=self.engine, checkfirst=False)
        self._log("Database created.")

    def destroy(self):
        """Drops all tables"""
        self.session.commit()
        Base.metadata.drop_all(bind=self.engine)

    def close(self):
        self.session.remove()

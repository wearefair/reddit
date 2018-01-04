"""
==========
Base Model
==========

All of our models extend this model. It adds comparisons by UUID to all our
models.
"""
from babel import Locale
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import i18n

i18n.get_locale = lambda: Locale('en')


class Base(object):
    def __repr__(self):
        result = self.__class__.__name__

        if hasattr(self, 'id'):
            result += ' {}'.format(self.id)

        for column in self.__table__.columns:
            if column.name == 'id':
                continue
            result += ' {}={}'.format(
                column.name,
                getattr(self, column.name, None))

        return '<{}>'.format(result)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if hasattr(self, 'id'):
                return self.id == other.id
            return super(Base, self).__eq__(other)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        if hasattr(self, 'id'):
            return id(self.id)
        return super(Base, self).__hash__()


Base = declarative_base(cls=Base)

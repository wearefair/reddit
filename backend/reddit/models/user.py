"""
==========
User Model
==========
"""
import string
import uuid

import nacl.utils
from sqlalchemy import (
    Column,
    String,
)
from sqlalchemy.orm import (
    validates,
)
from sqlalchemy_utils import (
    Password,
    PasswordType,
    UUIDType,
)

from .base import Base


DEFAULT_CHARSET = string.ascii_letters + string.digits + '!@#$%^&*()'


def secure_random_string(length=32, charset=None):
    charset = charset or DEFAULT_CHARSET
    charset_length = len(charset)

    def _get_char(byte):
        return charset[byte % charset_length]
    return "".join(map(_get_char, nacl.utils.random(length)))


def default_password():
    return secure_random_string(32)


class User(Base):
    """ Reddit User """

    __tablename__ = 'user'

    id = Column(
        UUIDType,
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
        doc="UUID for the object")

    username = Column(
        String,
        nullable=False,
        unique=True,
        doc="Username, typically the email address of the user",
    )

    email = Column(
        String,
        nullable=False,
        unique=True,
        doc="Email address of the user"
    )

    password = Column(
        PasswordType(schemes=['bcrypt']),
        nullable=False,
        default=default_password,
        doc="Bcrypt",
    )

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise ValueError("Username cannot be empty.")
        return username

    @validates('password')
    def validate_password(self, key, password):
        if isinstance(password, Password):
            return password

"""
==========
User Model
==========
"""
import uuid

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

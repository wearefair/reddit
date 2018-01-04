"""
===================
Topic Model
===================

"""

import arrow

from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Numeric
)
from sqlalchemy.orm import relationship

from sqlalchemy_utils import (
    ArrowType,
    UUIDType,
)

from .base import Base


class Topic(Base):
    """ Topic """

    __tablename__ = 'topic'

    id = Column(
        UUIDType,
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
        doc="UUID for the object")

    user_id = Column(
        UUIDType,
        ForeignKey('user.id'),
        nullable=True,
        doc="user.id of topic creator"
    )

    title = Column(
        String,
        nullable=False,
        doc="Title of topic"
    )

    title = Column(
        String,
        nullable=False,
        doc="Title of topic"
    )

    score = Column(
        Numeric(scale=2),
        default=1,
        nullable=False,
        doc="Topic score (net upvotes)"
    )

    heat_level = Column(
        Numeric(scale=2),
        default=1,
        nullable=False,
        doc="Topic hotness (activity level)"
    )

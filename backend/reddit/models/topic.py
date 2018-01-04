"""
===================
Topic Model
===================
"""
from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Numeric,
    Integer
)
from sqlalchemy_utils import (
    UUIDType,
)

from .base import Base
from .mixins import HasUUID, HasCreatedBy, HasCreatedAtUpdatedAt


class Topic(Base, HasUUID, HasCreatedBy, HasCreatedAtUpdatedAt):
    """ Topic """

    __tablename__ = 'topic'

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

    num_upvotes = Column(
        Integer,
        default=0,
        nullable=False,
        doc="Number of Upvotes"
    )

    num_downvotes = Column(
        Integer,
        default=0,
        nullable=False,
        doc="Number of Downvotes"
    )

    hotness_score = Column(
        Numeric(scale=2),
        default=1,
        nullable=False,
        doc="Topic hotness (activity level)"
    )

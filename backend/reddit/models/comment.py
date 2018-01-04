"""
=============
Comment Model
=============
"""
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Numeric,
    String,
)
from sqlalchemy.orm import backref, relationship

from sqlalchemy_utils import (
    UUIDType
)

from .base import Base
from .mixins import HasCreatedAtUpdatedAt, HasCreatedBy, HasUUID


class Comment(Base, HasUUID, HasCreatedAtUpdatedAt, HasCreatedBy):
    """Reddit comment"""

    __tablename__ = 'comment'

    content = Column(String, nullable=False, doc="Comment content")

    topic_id = Column(
        UUIDType,
        ForeignKey('topic.id'),
        nullable=False,
        doc="ID of the topic"
    )

    parent_comment_id = Column(
        UUIDType,
        ForeignKey('comment.id'),
        nullable=True,
        doc="ID of the topic"
    )

    parent = relationship("Comment", remote_side=[id])

    children = relationship("Comment", backref('parent', remote_side=[id]))

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

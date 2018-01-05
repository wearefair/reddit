"""
=============
Comment Model
=============
"""
import uuid

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
from .mixins import HasCreatedAtUpdatedAt, HasCreatedBy


class Comment(Base, HasCreatedAtUpdatedAt, HasCreatedBy):
    """Reddit comment"""

    __tablename__ = 'comment'

    id = Column(
            UUIDType,
            primary_key=True,
            default=uuid.uuid4,
            nullable=False,
            unique=True,
            doc="UUID for the object")

    content = Column(String, nullable=False, doc="Comment content")

    topic_id = Column(
        UUIDType,
        ForeignKey('topic.id'),
        nullable=False,
        doc="ID of the topic"
    )

    topic = relationship('Topic',
                         backref=backref('comments'))

    parent_comment_id = Column(
        UUIDType,
        ForeignKey('comment.id'),
        nullable=True,
        doc="ID of the topic"
    )

    children = relationship('Comment',
                            backref=backref('parent', remote_side=[id]))

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

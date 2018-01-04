import uuid

import arrow

from sqlalchemy import Column, ForeignKey
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship

from sqlalchemy_utils import ArrowType, UUIDType


class HasUUID(object):
    """
    Provides a UUID id if the model doesn't declare an ID field. All models
    should use this field so we have uniform object-ids and can more easily
    take advantage of generic relationships.
    """
    @declared_attr
    def id(self):
        return Column(
            UUIDType,
            primary_key=True,
            default=uuid.uuid4,
            nullable=False,
            unique=True,
            doc="UUID for the object")
    """UUID for the object"""

    @declared_attr
    def __repr__(self):
        return '<{} {}>'.format(self.__class__.__name__, self.id)


class HasCreatedAtUpdatedAt(object):
    @declared_attr
    def created_at(self):
        return Column(ArrowType,
                      default=arrow.utcnow,
                      nullable=False,
                      doc="Time the object was created")

    """Time the object was created."""

    @declared_attr
    def updated_at(self):
        return Column(ArrowType,
                      nullable=False,
                      default=arrow.utcnow,
                      onupdate=arrow.utcnow,
                      doc="Time the object was last updated")

    """Time the object was last updated."""


class HasCreatedBy(object):

    @declared_attr
    def created_by_id(self):
        """id of the user that created the given object."""
        return Column(UUIDType, ForeignKey('user.id'), nullable=False,
                      doc="id of the user that created the given object")

    @declared_attr
    def created_by(self):
        """User that created the given object."""
        return relationship('User', foreign_keys=[self.created_by_id],
                            doc="User that created the given object")
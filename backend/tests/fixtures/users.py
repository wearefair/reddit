import arrow
import pytest
import uuid

from reddit.models import (
    User,
)

@pytest.fixture(scope='function')
def test_user(db):
    user = User(
        username='test_user',
        email='fair-reddit-user@mailinator.com',
        password='testing',
    )
    user.id = uuid.uuid4()
    user.created_by_id = user.id
    db.add(user)
    db.commit()
    return user

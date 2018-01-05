import arrow
import pytest

from reddit.models import (
    Topic,
)

@pytest.fixture(scope='function')
def test_topics(db, test_user):
    result = []
    for i in range(10):
        topic = Topic(
            created_by=test_user,
            hotness_score=i,
            num_upvotes=i,
            title='Topic {}'.format(i),
        )
        db.add(topic)
        result.append(topic)
    db.commit()
    return result

@pytest.fixture(scope='function')
def test_controversial_topics(db, test_user):
    result = []
    for i in range(5):
        topic = Topic(
            created_by=test_user,
            hotness_score=i,
            num_upvotes=7,
            num_downvotes=5,
            title='Topic {}'.format(i),
        )
        db.add(topic)
        result.append(topic)
    db.commit()
    return result

@pytest.fixture(scope='function')
def test_search_topics(db, test_user):
    result = []
    for i in range(5):
        topic = Topic(
            created_by=test_user,
            hotness_score=i,
            num_upvotes=7,
            num_downvotes=5,
            title='Test Topics'.format(i),
        )
        db.add(topic)
        result.append(topic)
    db.commit()
    return result

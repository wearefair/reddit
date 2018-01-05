import os
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database

from reddit.models import (
    Base,
    User,
    Topic,
)

db_url=os.environ['DATABASE_URL']

engine = create_engine(db_url)
db = scoped_session(sessionmaker(autocommit=False,
                                 autoflush=False,
                                 bind=engine))

user = User(
    username='test_user',
    email='fair-reddit-user@mailinator.com',
    password='testing',
)
user.id = uuid.uuid4()
user.created_by_id = user.id
db.add(user)
db.commit()

for i in range(10):
  topic = Topic(
    created_by=user,
    hotness_score=i,
    num_upvotes=i,
    title='Topic {}'.format(i),
  )
  db.add(topic)

for i in range(11, 15):
  topic = Topic(
    created_by=user,
    hotness_score=2*i,
    num_upvotes=i,
    num_downvotes=i,
    title='Controversial Topic {}'.format(i),
  )
  db.add(topic)
db.commit()

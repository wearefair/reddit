from reddit.models import User

def get_default_user(db):
    return db.query(User).filter(User.username == 'test_user').first()

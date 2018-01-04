from reddit.models import Topic


def test_list_topics(app, db):
    res = app.get('/home')
    print(res)
    print("whoooo")
    assert True
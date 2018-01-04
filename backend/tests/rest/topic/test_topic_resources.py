import json

from reddit.models import Topic


def test_list_topics(app, db, test_topics):
    assert len(test_topics) == 10
    res = app.get('/home')
    assert res.status_code == 200
    response_json = json.loads(res.data)
    assert len(response_json) == len(test_topics)

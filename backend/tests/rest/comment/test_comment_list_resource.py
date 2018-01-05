import json

from reddit.models import (
    Comment,
)


def test_listing_comments(app, db, test_topics, test_user):
    for i in range(10):
        comment = Comment(
            topic=test_topics[0],
            created_by=test_user,
            num_upvotes=i,
            num_downvotes=i + 10,
            content='What a bunch of rubbish '
        )
        db.add(comment)

    c2 = Comment(
        topic=test_topics[0],
        parent=comment,
        created_by=test_user,
        num_upvotes=20,
        num_downvotes=0,
        content='I know!'
    )
    db.add(c2)
    db.commit()

    res = app.get('/comments/{}'.format(test_topics[0].id))
    assert res.status_code == 200

    print(res.data)
    data = json.loads(res.data)
    assert len(data) == 11
    assert any(d['parent_id'] is not None for d in data)


def test_creating_comment(app, db, test_topics, test_user):
    data = {
        'content': "Wow, what a weird weird system.",
        'parent_comment_id': None
    }

    res = app.post('/comments/{}'.format(test_topics[0].id),
                   data=json.dumps(data), content_type='application/json')
    assert res.status_code == 201
    data = json.loads(res.data)
    assert 'id' in data
    assert 'parent_id' in data
    assert 'content' in data

    res = app.get('/comments/{}'.format(test_topics[0].id))
    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data) == 1

    d2 = {
        'content': "Noo!",
        'parent_comment_id': data[0]['id']
    }
    res = app.post('/comments/{}'.format(test_topics[0].id),
                   data=json.dumps(d2), content_type='application/json')

    res = app.get('/comments/{}'.format(test_topics[0].id))
    assert res.status_code == 200
    data = json.loads(res.data)
    assert len(data) == 2
    assert any(d['parent_id'] is not None for d in data)

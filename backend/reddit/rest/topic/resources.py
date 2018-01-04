import json

from reddit.rest.resource import DetailResource, ListResource
from reddit.models import Topic
from flask import request, Response



class TopicListResource(ListResource):
    def get(self):
        resp = [
            {
                'id': topic.id,
                'title': topic.title,
                'user_id': topic.user_id,
                'num_upvotes': topic.num_upvotes,
                'num_downvotes': topic.num_downvotes,
                'hotness_score': topic.hotness_score,
                'created_by_id': topic.created_by_id,
                'created_at': topic.created_at,
                'updated_at': topic.updated_at
            } for topic in self.db.query(Topic).all()
        ]
        return Response(json.dumps(resp), mimetype='application/json')

    def post(self):
        args = request.form
        print(args)


import json

from reddit.rest.resource import DetailResource, ListResource
from reddit.models import Topic
from flask import request, Response



class TopicListResource(ListResource):
    def get(self):
        resp = [
            {
                'id': str(topic.id),
                'title': topic.title,
                'user_id': str(topic.user_id),
                'num_upvotes': int(topic.num_upvotes),
                'num_downvotes': int(topic.num_downvotes),
                'hotness_score': float(topic.hotness_score),
                'created_by_id': str(topic.created_by_id),
                'created_at': topic.created_at.isoformat(),
                'updated_at': topic.updated_at.isoformat(),
            } for topic in self.db.query(Topic).all()
        ]
        return Response(json.dumps(resp), mimetype='application/json')

    def post(self):
        args = request.form
        print(args)


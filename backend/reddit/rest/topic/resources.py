from reddit.rest.resource import DetailResource, ListResource
from reddit.models import Topic
from flask import request


class TopicListResource(ListResource):
    def list(self):
        return [
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

    def create(self):
        args = request.form
        print(args)


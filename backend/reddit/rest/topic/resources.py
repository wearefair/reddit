import json

from reddit.rest.resource import ListResource
from reddit.models import Topic
from flask import request, Response


class TopicRecentListResource(ListResource):
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
            } for topic in self.db.query(Topic).order_by(Topic.created_at.desc()).all()
        ]
        return Response(json.dumps(resp), mimetype='application/json')

    def post(self):
        args = request.form
        print(args)


class TopicControversialListResource(ListResource):
    def get(self):
        controversial_threshold = 5
        controversial_difference = 2
        all_topics = self.db.query(Topic).filter(
            Topic.num_upvotes >= controversial_threshold,
            Topic.num_downvotes >= controversial_threshold,
        ).order_by(Topic.created_at.desc()).all()
        filtered_topics = [t for t in all_topics if abs(t.num_upvotes -t.num_downvotes) >= controversial_difference]

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
            } for topic in filtered_topics
        ]
        return Response(json.dumps(resp), mimetype='application/json')

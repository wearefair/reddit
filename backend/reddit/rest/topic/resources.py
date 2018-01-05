import json

from reddit.rest.resource import ListResource
from reddit.models import Topic, User
from flask import request, Response


class TopicListResource(ListResource):
    def get(self):

        resp = [
            {
                'id': str(topic.id),
                'title': topic.title,
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
        """
        Example curl:
        `curl -H "Content-Type: application/json" -X POST -d '{"title": "test"}' http://127.0.0.1:5000/home`
        """
        args = request.json
        print(args)
        topic = Topic(
            title=args['title'],
            created_by=self.db.query(User).first(),
        )

        self.db.add(topic)
        self.db.commit()
        return Response(json.dumps({
                'id': str(topic.id),
                'title': topic.title,
                'created_by': {
                    'id': str(topic.created_by_id),
                    'email': topic.created_by.email,
                },
                'num_upvotes': int(topic.num_upvotes),
                'num_downvotes': int(topic.num_downvotes),
                'hotness_score': float(topic.hotness_score),
                'created_at': topic.created_at.isoformat(),
            }),  mimetype='application/json'
        ), 201


class TopicControversialListResource(ListResource):
    def get(self):
        controversial_threshold = 5
        controversial_difference = 2
        all_topics = self.db.query(Topic).filter(
            Topic.num_upvotes >= controversial_threshold,
            Topic.num_downvotes >= controversial_threshold,
        ).order_by(Topic.created_at.desc()).all()
        filtered_topics = [
            t for t in all_topics
            if abs(t.num_upvotes - t.num_downvotes) <= controversial_difference
        ]

        resp = [
            {
                'id': str(topic.id),
                'title': topic.title,
                'num_upvotes': int(topic.num_upvotes),
                'num_downvotes': int(topic.num_downvotes),
                'hotness_score': float(topic.hotness_score),
                'created_by_id': str(topic.created_by_id),
                'created_at': topic.created_at.isoformat(),
                'updated_at': topic.updated_at.isoformat(),
            } for topic in filtered_topics
        ]
        return Response(json.dumps(resp), mimetype='application/json')


class TopicSearchListResource(ListResource):
    def get(self):
        search = request.args.get('search', '')
        resp = [
            {
                'id': str(topic.id),
                'title': topic.title,
                'num_upvotes': int(topic.num_upvotes),
                'num_downvotes': int(topic.num_downvotes),
                'hotness_score': float(topic.hotness_score),
                'created_by_id': str(topic.created_by_id),
                'created_at': topic.created_at.isoformat(),
                'updated_at': topic.updated_at.isoformat(),
            } for topic in self.db.query(Topic).filter(
                    Topic.title == search
                ).order_by(Topic.created_at.desc()).all()
        ]
        return Response(json.dumps(resp), mimetype='application/json')

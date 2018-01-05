import json

from flask import Response, request

from reddit.models import Comment
from reddit.rest.resource import ListResource


class CommentListResource(ListResource):
    def get(self, id):
        resp = [
            {
                'id': str(comment.id),
                'content': comment.content,
                'parent_id': str(comment.parent_comment_id)
                if comment.parent_comment_id else None,
                'created_by': {
                    'id': str(comment.created_by_id),
                    'email': comment.created_by.email,
                },
                'num_upvotes': int(comment.num_upvotes),
                'num_downvotes': int(comment.num_downvotes),
                'hotness_score': float(comment.hotness_score),
                'created_at': comment.created_at.isoformat(),
                'updated_at': comment.updated_at.isoformat(),
            } for comment in self.db.query(Comment).filter(
                Comment.topic_id == id).all()
        ]
        return Response(json.dumps(resp), mimetype='application/json')

    def post(self):
        args = request.form
        print(args)

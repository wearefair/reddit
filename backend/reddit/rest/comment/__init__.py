from reddit.rest.comment.comment_list_resource import (
    CommentListResource
)
from reddit.rest.route import Route

routes = [
    Route('/comments/<string:id>',
          CommentListResource.as_view('comment_resource'))
]

__all__ = [
    'routes',
]

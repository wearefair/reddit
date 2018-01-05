from reddit.rest.route import Route
from reddit.rest.topic.resources import (
    TopicListResource,
    TopicControversialListResource,
)

routes = [
    Route('/home', TopicListResource.as_view('topic_list_resource')),
    Route('/home/recent', TopicListResource.as_view('topic_list_recent_resource')),
    Route('/home/controversial', TopicControversialListResource.as_view('topic_list_controversial_resource'))

]

__all__ = [
    'routes',
]

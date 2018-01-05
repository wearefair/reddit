from reddit.rest.route import Route
from reddit.rest.topic.resources import (
    TopicControversialListResource,
    TopicRecentListResource
)

routes = [
    Route('/home/recent', TopicRecentListResource.as_view('topic_recent_resource')),
    Route('/home/controversial', TopicControversialListResource.as_view('topic__controversial_resource'))

]

__all__ = [
    'routes',
]

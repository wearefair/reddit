from reddit.rest.route import Route
from reddit.rest.topic.resources import TopicListResource

routes = [
    Route('/home', TopicListResource)
]

__all__ = [
    'routes',
]

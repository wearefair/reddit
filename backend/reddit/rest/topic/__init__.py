from reddit.rest.route import Route
from reddit.rest.topic.resources import TopicListResource

routes = [
    Route('/home', TopicListResource.as_view('topic_resource'))
]

__all__ = [
    'routes',
]

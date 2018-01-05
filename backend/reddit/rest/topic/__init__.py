from reddit.rest.route import Route
from reddit.rest.topic.resources import (
    TopicListResource,
    TopicControversialListResource,
    TopicSearchListResource
)

routes = [
    Route('/home', TopicListResource.as_view('topic_list_resource')),
    Route('/home/recent', TopicListResource.as_view('topic_list_recent_resource')),
    Route('/home/controversial', TopicControversialListResource.as_view('topic_list_controversial_resource')),
    Route('/home/search', TopicSearchListResource.as_view('topic_search_resource'))
]

__all__ = [
    'routes',
]

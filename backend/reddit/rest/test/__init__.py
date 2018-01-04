from reddit.rest.route import Route

from reddit.rest.test.resources import serve_one

routes = [
    Route('/test', serve_one)
]

__all__ = [
    'routes',
]

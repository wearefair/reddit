from reddit.rest.topic import routes as topic_routes

ALL_ROUTES = [
    topic_routes
]


def initialize(app):
    for endpoints in ALL_ROUTES:
        for route in endpoints:
            app.add_url_rule(route.path, view_func=route.handler)

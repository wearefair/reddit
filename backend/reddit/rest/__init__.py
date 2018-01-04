from reddit.rest.test import routes as test_routes

ALL_ROUTES = [
    test_routes
]


def initialize(app):
    for endpoints in ALL_ROUTES:
        for route in endpoints:
            app.route(route.path)(route.handler)

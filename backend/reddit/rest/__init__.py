from reddit.rest.test import serve_one

def initialize(app):
    app.route('/test')(serve_one)


import logging

from flask import (
    request,
    views,
)
from reddit.rest.exceptions import (
    ApiError,
    BadRequest,
    MethodNotAllowed,
    RequestTooLarge
)
from sqlalchemy.exc import (
    IntegrityError,
    StatementError,
)

MAX_CONTENT_LENGTH = 0.5 * 1024 * 1024
logger = logging.getLogger(__name__)


class Resource(views.MethodView):
    representations = None
    max_content_length = MAX_CONTENT_LENGTH

    def dispatch_request(self, *args, **kwargs):
        if 'location' in request.path:
            length = request.content_length
            if length is not None and length > self.max_content_length:
                raise RequestTooLarge('{} must be less than {}'.format(
                    length, self.max_content_length))

        method = self.__class__.__dict__.get(request.method.lower(), None)
        if method is None and request.method == 'HEAD':
            method = self.__class__.__dict__.get('get', None)
        if method is None:
            raise MethodNotAllowed("{} not supported for {}".format(
                request.method, request.path))

        try:
            resp = method(self, *args, **kwargs)
        except ApiError as e:
            logger.info("Endpoint handled error when calling method!")
            raise e
        except (StatementError, IntegrityError) as e:
            logger.exception("Endpoint failed to handle database error!")
            message = getattr(e, 'message', str(e))
            metadata = getattr(e, 'metadata', {})
            raise BadRequest(message, payload=metadata)
        except Exception as e:
            logger.exception("Endpoint failed to handle other error!")
            raise BadRequest('Something went wrong :(')

        return resp


class DetailResource(Resource):
    def get(self, **kwargs):
        return self.fetch(**kwargs)

    def put(self, **kwargs):
        return self.update(**kwargs)

    def delete(self, **kwargs):
        return self.destroy(**kwargs)

    def fetch(self, **kwargs):
        raise MethodNotAllowed('Subclasses must implement method "fetch"')

    def update(self, **kwargs):
        raise MethodNotAllowed('Subclasses must implement method "update"')

    def destroy(self, **kwargs):
        raise MethodNotAllowed('Subclasses must implement method "destroy"')


class ListResource(Resource):
    def get(self, **kwargs):
        return self.list(**kwargs)

    def post(self, **kwargs):
        resp = self.create(**kwargs)
        if resp.status_code == 200:
            resp.status_code = 201
        return resp

    def create(self, **kwargs):
        raise MethodNotAllowed('Subclasses must implement method "create"')

    def list(self, **kwargs):
        raise MethodNotAllowed('Subclasses must implement method "list"')

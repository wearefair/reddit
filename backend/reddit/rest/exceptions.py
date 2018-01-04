class ApiError(Exception):
    """
    Base API Error, all errors should extend from this.
    """
    status_code = 400

    def __init__(self, message, payload=None, title=None):
        super(ApiError, self).__init__()
        self.message = message
        self.title = title or "Invalid Request"
        self.payload = payload or {}
        self.type = self.__class__.__name__

    def to_dict(self):
        return dict(
            payload=self.payload,
            title=self.title,
            message=self.message,
            type=self.type,
            status=self.status_code
        )


class AuthenticationError(ApiError):
    """
    Thrown when the user isn't logged in
    """
    status_code = 401


class Forbidden(ApiError):
    """
    Thrown when the user is logged in, but doesn't have sufficient permissions
    to do the desired action.
    """
    status_code = 403


class MethodNotAllowed(ApiError):
    """
    Thrown when a NotImplemented exception is thrown.
    """
    status_code = 405


class ObjectAlreadyExists(ApiError):
    """
    Thrown when an attempting to create an object and an IntegrityError is
    thrown.
    """
    status_code = 409


class ObjectNotFound(ApiError):
    """
    Thrown when an attempting to retrieve an object that does not exist.
    """
    status_code = 404


class ObjectLocked(ApiError):
    """
    Thrown when an attempting to modify an object that is in the process of
    being modified.
    """
    status_code = 409


class BadRequest(ApiError):
    """
    Thrown when we get extra or invalid data sent to an API endpoint.
    """
    status_code = 400


class RequestTooLarge(ApiError):
    status_code = 413

    def __init__(self, message):
        title = 'Request Too Large'
        super(RequestTooLarge, self).__init__(message, {}, title)


class InvalidUserData(BadRequest):
    """
    Thrown when we get extra or invalid data in a field sent to an endpoint.
    """
    def __init__(self, msg, field):
        """
        Use like so:
        .. code-block:: python
           if args['tiers'] is None:
               raise InvalidUserData("Can't pass in 'None' for email!",
                                      'email')
        :param msg: Error message
        :param field: Name of the argument field causing issues
        """
        params = {
            'fields': {
                field: msg
            }
        }
        super(InvalidUserData, self).__init__(msg, payload=params)

from rest_framework import status
from rest_framework.response import Response


class BasicApiError:
    ERROR_CODE = "Error"
    STATUS_CODE = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, detail_message=None, status_code=None):
        self.status_code = status_code if status_code is not None else self.STATUS_CODE
        self.detail_message = "" if detail_message is None else detail_message

    def __call__(self):
        # This will return an DRF response with specified status code
        data = {
            'error': self.ERROR_CODE,
            'message': self.detail_message
        }
        return Response(data=data, status=self.status_code)


class MissingInputError(BasicApiError):
    ERROR_CODE = "Missing Input Error"
    STATUS_CODE = status.HTTP_400_BAD_REQUEST


class AlreadyExistError(BasicApiError):
    ERROR_CODE = "Already exist Error"
    STATUS_CODE = status.HTTP_400_BAD_REQUEST


class ObjectNotExistError(BasicApiError):
    ERROR_CODE = "Object not exist"
    STATUS_CODE = status.HTTP_400_BAD_REQUEST
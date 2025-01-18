import logging

logger = logging.getLogger('gunicorn_logger')

class WSGIRequestLoggerMiddleware:
    '''This middleware is used to check request info while
    reaching to WSGI server before entering view process
    '''
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        # Log request information
        logger.info(f"""
Request received:
- Method: {environ.get('REQUEST_METHOD')}
- Path: {environ.get('PATH_INFO')}
- Query: {environ.get('QUERY_STRING')}
- Headers: {[(k, v) for k, v in environ.items()]}
""")

        return self.wsgi_app(environ, start_response)

bind = "0.0.0.0:8000"  # IP and port to bind
workers = 2  # Number of worker processes
threads = 8
worker_class = "gthread"
timeout = 120  # Worker timeout in seconds
graceful_timeout = 30
max_requests = 8192
reload = False

errorlog = '/app/gunicorn_log/gunicorn-error.log'
accesslog = '/app/gunicorn_log/gunicorn-access.log'
loglevel = 'warning'

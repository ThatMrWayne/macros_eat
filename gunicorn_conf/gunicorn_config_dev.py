bind = "0.0.0.0:8000"  # IP and port to bind
workers = 2  # Number of worker processes
threads = 8
worker_class = "gthread"
timeout = 120  # Worker timeout in seconds
graceful_timeout = 30
max_requests = 8192
reload = True # for dev

errorlog = '/app/log/gunicorn-error.log'
accesslog = '/app/log/gunicorn-access.log'
loglevel = 'info'

import logging
from logging.config import dictConfig
from functools import wraps

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})


def with_logging(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info('Running job "%s"' % func.__name__)
        func(*args, **kwargs)
        logging.info('Job "%s" completed' % func.__name__)

    return wrapper

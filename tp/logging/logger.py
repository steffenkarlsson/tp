from logging import getLogger as logging_getLogger
from logging import config
from logging import DEBUG as LOGGING_DEBUG

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s Module:%(module)s: %(message)s'
            },
        },
    'handlers': {
        'tp-logger': {
            'class': 'logging.handlers.SysLogHandler',
            'address': '/dev/log',
            'facility': 'local6',
            'formatter': 'verbose',
            },
        },
    'loggers': {
        'tp-logger': {
            'handlers': ['tp-logger'],
            'level': LOGGING_DEBUG,
            'propagate': True,
            },
        }
    }
config.dictConfig(LOGGING)


def get_logger():
    return logging_getLogger("tp-logger")
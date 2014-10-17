from vdw.conf.settings import *  # noqa

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'varifydb',
    },
}

INSTALLED_APPS = (
    'tests',
    'tests.cases.south_tests',
    'tests.cases.sample_load_process',
    'tests.cases.commands',

    'vdw',

    'vdw.assessments',
    'vdw.genes',
    'vdw.genome',
    'vdw.phenotypes',
    'vdw.samples',
    'vdw.variants',

    'vdw.assessments',
    'vdw.genes',
    'vdw.genome',
    'vdw.literature',
    'vdw.phenotypes',
    'vdw.samples',
    'vdw.variants',

    'south',
    'guardian',
    'django_rq',
    'sts',
    'reversion',

    'avocado',
    'avocado.export',
    'modeltree',

    # built-in Django apps
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
)

TEST_RUNNER = 'tests.runner.ProfilingTestRunner'
TEST_PROFILE = 'unittest.profile'

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
    'samples': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
    'variants': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
    'effects': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
    'results': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'rq_console': {
            'format': '%(asctime)s %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler'
        },
        'rq_console': {
            'level': 'DEBUG',
            'class': 'rq.utils.ColorizingStreamHandler',
            'formatter': 'rq_console',
            'exclude': ['%(asctime)s'],
        }
    },
    'loggers': {
        'vdw': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'tests': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'rq.worker': {
            'handlers': ['rq_console'],
            'level': 'DEBUG',
        },
    }
}

SOUTH_TESTS_MIGRATE = False

SECRET_KEY = 'acb123'

VDW_GENOME_VERSION = 'hg19'

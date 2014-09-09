import os

# Import global settings to make it easier to extend settings.
from django.conf.global_settings import *  # noqa

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Import the project module to calculate directories relative to the module
# location.
PROJECT_PATH = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                            '../..')

# List all Django apps here. Note that standard Python libraries should not
# be added to this list since Django will not recognize them as apps anyway.
# An app is really only an "app" if a `models` module or package is defined.
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',

    'vdw',

    'vdw.raw',
    'vdw.raw.sources',

    'vdw.assessments',
    'vdw.genome',
    'vdw.genes',
    'vdw.variants',
    'vdw.phenotypes',
    'vdw.samples',
    'vdw.literature',

    'vdw.pipeline',


    'south',
    'guardian',
    'django_rq',
    'avocado',
    'avocado.export',
    'modeltree',
    'reversion',
)


#
# ADMINISTRATIVE
#

# Admins receive any error messages by email if DEBUG is False
ADMINS = ()

# Managers receive broken link emails if SEND_BROKEN_LINK_EMAILS is True
MANAGERS = ADMINS

# List of IP addresses which will show debug comments
INTERNAL_IPS = ('127.0.0.1', '::1')

#
# DATABASES
# Each database can be specified here, but passwords should be in a separate
# file that is not versioned. Use ``local_settings.py``.
#

DATABASES = {}

# Database routers can useful for delegating database operations transparently
# to different databases depending on what data is being acted on. For Harvest
# instances that make use of an existing database, it is typically never
# desirable to create all the Harvest application tables in this database, but
# rather have a separate database for this purpose. That way the "data"
# database does not need to be changed.

DATABASE_ROUTERS = {}


#
# LOCALITY
#

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = None

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = False


#
# STATIC AND MEDIA
# The application's static files should be placed in the STATIC_ROOT in
# addition to other static files found in third-party apps. The MEDIA_ROOT
# is intended for user uploaded files.
#

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_PATH, '_site/media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PROJECT_PATH, '_site/static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
STATICFILES_DIRS = ()

#
# TEMPLATES
#

# Project level templates and template directories that override
# third-party app templates.
TEMPLATE_DIRS = ()

#
# URLS
#

# FORCE_SCRIPT_NAME overrides the interpreted 'SCRIPT_NAME' provided by the
# web server. since the URLs below are used for various purposes outside of
# the WSGI application (static and media files), these need to be updated to
# reflect this discrepancy.
FORCE_SCRIPT_NAME = ''

# For non-publicly accessible applications, the siteauth app can be used to
# restrict access site-wide.
SITEAUTH_ACCESS_ORDER = 'allow/deny'

SITEAUTH_ALLOW_URLS = ()

#
# MIDDLEWARE
#

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'reversion.middleware.RevisionMiddleware',
)

#
# EMAIL
#

EMAIL_SUBJECT_PREFIX = '[Varify-Data-Warehouse] '
NO_REPLY_EMAIL = 'noreply@example.com'
SUPPORT_EMAIL = 'support@example.com'

#
# LOGGING
#

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


#
# CACHE
#

# For production environments, the memcached backend is highly recommended
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'vdw',
        'VERSION': 1,
    },
    'vdw.pipeline': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'vdw.pipeline',
        'VERSION': 1,
    }
}

# Default cache seconds for a resource, use the `cache_page` decorator to
# change the amount of time for a given resource.
CACHE_MIDDLEWARE_SECONDS = 60

# This is not necessary to set if the above `KEY_PREFIX` value is set since
# the `KEY_PREFIX` namespaces all cache set by this application
CACHE_MIDDLEWARE_KEY_PREFIX = ''

# For django-guardian
ANONYMOUS_USER_ID = -1

MODELTREES = {
    'default': {
        'model': 'samples.result',
        'excluded_models': ['avocado.datacontext'],
        'required_routes': [{
            'target': 'genes.gene',
            'source': 'genes.transcript',
        }, {
            'target': 'samples.cohort',
            'source': 'samples.cohortvariant',
        }, {
            'source': 'genes.gene',
            'target': 'genes.genephenotype',
        }, {
            'target': 'samples.cohortvariant',
            'source': 'variants.variant',
        }],
        'excluded_routes': [{
            'target': 'genes.gene',
            'source': 'literature.pubmed',
            'symmetrical': True,
        }],
    },
}

AVOCADO = {
    'METADATA_MIGRATION_APP': 'vdw',
}

VARIFY_SAMPLE_DIRS = ()

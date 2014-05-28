import socket
# Django settings for d8adotcom project.

DEPLOYMENT_TIMESTAMP = 1375820124 

DEBUG = True
TEMPLATE_DEBUG = DEBUG

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'no-reply@metalayer.com'
EMAIL_HOST_PASSWORD = '##M3taM3ta'
EMAIL_PORT = 587

ADMINS = (
    ('Jon G.', 'jon@d8a.com'),
)

MANAGERS = ADMINS

# Seems to be unused
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.mysql' if not socket.gethostname() in ['Jonathan-Gosiers-MacBook-Air.local','localhost','Jons-MacBook-Air.local'] else '', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        'NAME': 'ml_prod_corporate', # Or path to database file if using sqlite3.
#        'USER': 'root',                      # Not used with sqlite3.
#        'PASSWORD': '' if socket.gethostname() in ['mattgriffiths'] else '##M3taM3ta',                  # Not used with sqlite3.
#        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': 3306,                      # Set to empty string for default. Not used with sqlite3.
#    }
#}


# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = '502bf82cc845b31bb300001d'

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    '/usr/local/metaLayer-metalayerdotcom/metalayerdotcom/static/',
    '/Users/Gosier/Code/metaLayer-metalayerdotcom/static/',
	'/Users/metalayer/Virtualenvs/sites/d8adotcom/static/',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#   'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'u!^hg@f_g7y=!f%u54276_zkq)azlgs_0-w%$qpz)k!obg^56('

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'middleware.multihostmiddleware.MultiHostMiddleware',
)

# Change Primary Site
ROOT_URLCONF = 'd8a.urls'

HOST_MIDDLEWARE_URLCONF_MAP = {	

	'local.appfrica.com:8000':'appfrica.urls',
	'www.appfrica.com':'appfrica.urls',
	'appfrica.com':'appfrica.urls',
	
	'local.abayima.com:8000':'abayima.urls',
	'www.abayima.com':'abayima.urls',
	'abayima.com':'abayima.urls',

    'local.d8a.com:8000':'d8a.urls',
    'www.d8a.com':'d8a.urls',
    'd8a.com':'d8a.urls',

	'local.apps4africa.org:8000':'apps4africa.urls',
    'www.apps4africa.org':'apps4africa.urls',
    'apps4africa.org':'apps4africa.urls',

	'local.fund.appfrica.com:8000':'apps4africa.urls',
    'fund.appfrica.com':'apps4africa.urls',

	'local.gosfellowship.com:8000':'gos.urls',
    'www.gosfellowship.com':'gos.urls',
    'gosfellowship.com':'gos.urls',

	'local.statfrica.com:8000':'appfrica.urls',
    'www.statfrica.com':'appfrica.urls',
    'statfrica.com':'appfrica.urls',

	'local.upstream-analytics.com:8000':'upstream.urls',
    'www.upstream-analytics.com':'upstream.urls',
    'upstream-analytics.com':'upstream.urls',

}

TEMPLATE_DIRS = (
    '/usr/local/metaLayer-metalayerdotcom/metalayerdotcom/static/html',
    '/Users/Gosier/Code/metaLayer-metalayerdotcom/static/html',
	'/Users/metalayer/Virtualenvs/sites/d8adotcom/static/html',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    'django.contrib.messages.context_processors.messages',
    "contextprocessors.settings.context_settings",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'contextprocessors',
    'customtags',
    'd8a',
)

#SENTRY_DSN = 'http://6466cf51ea014f3ba49e6ac623458c31:6b2dd5120fa54883a20d52b464aa8b35@108.166.111.61:9000/8'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
        },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        },
    'handlers': {
        'sentry': {
            'level': 'DEBUG',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'WARNING',
            'handlers': ['console'],
            'propagate': False,
            },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
            },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
            },
        },
    }

ENABLE_ANALYTICS = True

import socket
if socket.gethostname() in ['GRIFF-LINUX2']:
    from settings_matt import *

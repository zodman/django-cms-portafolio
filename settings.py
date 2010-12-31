# Django settings for interalia project.
import os
BASE_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'interalia',                      # Or path to database file if using sqlite3.
        'USER': 'desarrolloweb',                      # Not used with sqlite3.
        'PASSWORD': '123456',                  # Not used with sqlite3.
        'HOST': '10.0.0.2',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Mexico'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'es'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = BASE_PATH + '/media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '7mv@iac#wb%40(v17m)ck_0^hkpi^#f6q@w$3+r4acfxnq6cd7'

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
    "cms.middleware.media.PlaceholderMediaMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "cms.context_processors.media",
)



ROOT_URLCONF = 'interalia.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    BASE_PATH + "/templates/"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    #django apps
    'south',
    "sorl.thumbnail",
    #django-cms
    'cms',
#    'publisher',
    'mptt',
    'menus',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.snippet',
   'cms.plugins.googlemap',
    'cms.plugins.teaser',
    'cms.plugins.video',
    'cms.plugins.twitter',
    'cms.plugins.inherit',
    # custom cmsplugins
    "cmsplugin_facebook",
    #custom cmsapps
    "portafolio",
)
# django-cms settings
gettext = lambda s: s

CMS_TEMPLATES = (
        ('pagina_inicio.html', gettext('Pagina Inicio')),
        ('pagina_casos.html', gettext('Pagina Casos')),
        ('pagina_soluciones.html', gettext('Pagina Soluciones')),
)

CMS_MEDIA_ROOT = os.path.join(BASE_PATH, 'media/cms/')

CMS_SITE_LANGUAGES = {
        1:['es'],
}
CMS_MODERATOR = False 
GOOGLE_MAPS_API_KEY = "ABQIAAAA__ShXMvquJtWn_N18hRhhBRdlxeguhVb5aDTQiWeXVdMbc2yzxShEZQi_xkawQWnvbqGT20Lf2Db5A"

try:
    from local_settings import *
except ImportError: #FIX para el syncdb
    pass

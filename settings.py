# -*- coding: utf-8 -*-
# Django settings for Special Project CMS.
import os

location = lambda x: os.path.join(os.path.dirname(os.path.realpath(__file__)), x)

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = location("public/media")

MEDIA_URL = '/public/media/'

STATIC_ROOT = location("public/static")

STATIC_URL = '/public/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    location("static"),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!l-g1kbtxe8r@%0k&amp;j7*^tv)mo_18rza_f*+wl7nhuk5if_g!m'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'social_auth.middleware.SocialAuthExceptionMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'wsgi.application'

TEMPLATE_DIRS = (
    location('templates'),
)

# Defines subdirectory of templates directory with templates for the project
TEMPLATE_THEME = 'default'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'sorl.thumbnail',
    'social_auth',
    'ckeditor',
    'south',
    'sp.frontend',
    'sp.users',
    'sp.contest',
    'sp.quiz',
    'sp.publications',
    'sp.qa',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'social_auth.context_processors.social_auth_by_name_backends',
)

AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    'social_auth.backends.contrib.vk.VKOAuth2Backend',
    'social_auth.backends.contrib.odnoklassniki.OdnoklassnikiBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    #'social_auth.backends.contrib.mailru.MailruOAuth2',
    'backends.EmailAuthBackEnd',
    'django.contrib.auth.backends.ModelBackend',
)

AUTH_PROFILE_MODULE = 'users.UserProfile'

SOCIAL_AUTH_PIPELINE = (
    'social_auth.backends.pipeline.social.social_auth_user',
    'social_auth.backends.pipeline.associate.associate_by_email',
    'social_auth.backends.pipeline.user.get_username',
    'social_auth.backends.pipeline.user.create_user',
    'social_auth.backends.pipeline.social.associate_user',
    'social_auth.backends.pipeline.social.load_extra_data',
    'social_auth.backends.pipeline.user.update_user_details',
    'sp.users.social_auth_pipeline.get_user_avatar',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
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

FROM_EMAIL = 'special@webprimegroup.ru'

LOGIN_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/'

# Social Auth accounts settings
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''
VK_APP_ID = ''
VKONTAKTE_APP_ID = VK_APP_ID
VK_API_SECRET = ''
VKONTAKTE_APP_SECRET = VK_API_SECRET
ODNOKLASSNIKI_OAUTH2_CLIENT_KEY = ''
ODNOKLASSNIKI_OAUTH2_CLIENT_SECRET = ''
ODNOKLASSNIKI_OAUTH2_APP_KEY = ''
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

SOCIAL_AUTH_PROTECTED_USER_FIELDS = ['email', 'first_name', 'last_name',]

# CKEditor settings
CKEDITOR_UPLOAD_PATH = location("public/media/uploads")

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'Full',
    },
}

try:
    from settings_local import *
except ImportError:
    pass

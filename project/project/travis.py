from . import settings
import os
import dj_database_url
import django_heroku
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = '%_uznehy!@e-(g5%ubafz4jvtd(iz(=g%x0%zj&km09ktj&-^6'

ALLOWED_HOSTS = ['127.0.0.1', 'project8-elodiemeunier.herokuapp.com']

# This is defined here as a do-nothing function because we can't import
# django.utils.translation -- that module depends on the settings.
def gettext_noop(s):
    return s


# Application definition
INSTALLED_APPS = [
    'api_food.apps.ApiFoodConfig',
    'home.apps.HomeConfig',
    'user.apps.UserConfig',
    'product.apps.ProductConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = ['127.0.0.1']

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    },
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
LANGUAGE_CODE = 'fr'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale'),)

LANGUAGES = (
    ('fr', gettext_noop('French')),
    ('en', gettext_noop('English')),
)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'home', 'static'),
    os.path.join(BASE_DIR, 'user', 'static'),
    os.path.join(BASE_DIR, 'product', 'static'),
)

# Config auth model
AUTH_USER_MODEL = "user.User"
LOGIN_REDIRECT_URL = 'user:my_account'
AUTHENTICATION_BACKENDS = ['user.backends.EmailBackend']

"""
    FUNCTIONALS TESTS_

    To get the chromedriver : https://chromedriver.chromium.org/

    Change SELENIUM_DRIVER_PATH variable by your path if you can test
    - MACOS/LINUX = '/Your/path/driver/chromedriver'
    - WINDOWS = '/Your/path/driver/chromedriver.exe'
"""
SELENIUM_DRIVER = 'Chrome'

if os.environ.get('ENV'):
    if os.environ['ENV'] != 'PROD':
        SELENIUM_DRIVER_PATH = os.environ['DRIVER_PATH']

    if os.environ['ENV'] == 'PROD':
        django_heroku.settings(locals())

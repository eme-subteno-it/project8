from .config import *


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

# Management email for tests
EMAIL_HOST = 'smtp.office365.com'
EMAIL_HOST_USER = 'from@email.com'
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'from@email.com'

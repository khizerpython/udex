from udex.settings.base import *

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME'),
        'USER': os.environ.get('DATABASE_USER'),
        'PASSWORD': os.environ.get('DATABASE_USER_PASSWORD'),
        'HOST': os.environ.get('DATABASE_HOST'),
        'PORT': os.environ.get('DATABASE_PORT'),
    },
    
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/
ALLOWED_HOSTS = json.loads(os.environ.get("DJANGO_ALLOWED_HOSTS", []))


SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "test-Key")
STATIC_URL = 'static/'
STATIC_ROOT = STATIC_CUSTOM_DIR

DEBUG = False


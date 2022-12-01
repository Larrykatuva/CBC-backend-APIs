from pathlib import Path
import environ
import os
from django.contrib import messages
from datetime import timedelta

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(g-87)gh&!u(3e1g9ryy*81$tu9+ikdxm4y$oth&z@%gh!mg*o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

AUTH_USER_MODEL = 'src.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'src',
    'drf_yasg',
    'django_filters',
    'rest_framework'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


DATABASES = {
    'default': env.db()
}


REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 100,
    'NON_FIELD_ERRORS_KEY': 'error',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=30)
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# EMAIL_HOST = env.get_value('EMAIL_HOST')
# EMAIL_HOST_USER = env.get_value('EMAIL_HOST_USER')
# EMAIL_USE_TLS = env.get_value('EMAIL_USE_TLS')
# DEFAULT_FROM_EMAIL = env.get_value('DEFAULT_FROM_EMAIL')
# EMAIL_PORT = env.get_value('EMAIL_PORT')
# EMAIL_HOST_PASSWORD = env.get_value('EMAIL_HOST_PASSWORD')

EMAIL_HOST = 'smtp.zoho.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'support@kurasa.co'
DEFAULT_FROM_EMAIL = 'support@kurasa.co'
EMAIL_HOST_PASSWORD = 'agB8+J8n5BKqn_u'
EMAIL_USE_TLS = True

SINGLE_URL = env.get_value('SINGLE_URL')
MULTIPLE_URL = env.get_value('MULTIPLE_URL')
AUTH_KEY = 'AAAAwltgVL4:APA91bHtOxFsT-AVWnzheii1vbjfAdHOPkrUNosYTbPOcCeam1ZohkKIYaLqSwkwxZoXcXj-GHmr3bWBSykzBzmgCdCcfyq58tKtkP-I5cII20tLipddot8qHikEjv2FbFCHc2248mwd'


MESSAGE_TAGS = {
    messages.ERROR: 'danger'
}

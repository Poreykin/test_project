import os
#from .social_auth import *

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '=7z6r&pz-&qdwba7)8kzh3+lq4sy$vi1g_k1lqq)559vu$up9y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django_celery_beat',
    'django_celery_results',
    'stdimage',
    'imagekit',
    'webpack_loader',
    'cloudpayments',
    'mptt',
    'rest_framework',
    'django_fsm',
    'paypalrestsdk',
    'service_objects',
    #'social.apps.django_app.default',
    #'social.apps.django_app.urls',
    'test1.authentification',
    'test1.crud',
    'test1.gallery',
    'test1.payment',
    'test1.courses',
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

ROOT_URLCONF = 'test1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'test1', 'templates')],
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

WSGI_APPLICATION = 'test1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Yekaterinburg'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Email settings
AUTH_USER_EMAIL_UNIQUE = False # for testing purposes

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'gliwick@gmail.com'
EMAIL_HOST_PASSWORD = 'secret2901'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'gliwick@gmail.com'


# Celery settings
CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE


# PayPal settings
PAYPAL_CLIENT_ID = "AYC0aWHLKVnQkuFMdnPZfIz5J2VR4lTmM9ghU_szP9QT95xkWo0NQZNZ6Rme11MSw9P9SCejMfhSlakU"
PAYPAL_CLIENT_SECRET = "EAu4fR7ccEdPU8Np-5ljZOaEyReXM-nC5Aetwdz_uiGef6ZeUc11plBjAso3BeNAj_Tc_0WnfCn8m2e9"


# Media settings
MEDIA_ROOT = os.path.join(BASE_DIR, 'test1', 'media')
MEDIA_URL = '/media/'


# Webpacker settings
WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'test1/static'),
]

LOGIN_REDIRECT_URL = '/articles/view'

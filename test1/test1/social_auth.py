SOCIAL_AUTH_USER_MODEL = 'auth.User'

SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'

AUTHENTICATION_BACKENDS = (
    'social.backends.facebook.vk.VKOAuth2',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
)

# Проверка url перенаправления
SOCIAL_AUTH_SANITIZE_REDIRECTS = True

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']
SOCIAL_AUTH_VK_OAUTH2_API_VERSION = '5.5'
SOCIAL_AUTH_VK_OAUTH2_KEY = 'VK_APP_ID'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'VK_APP_SECRET'

# django_project/settings/basic.py
from .social_auth import *
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'social.apps.django_app.default',
)

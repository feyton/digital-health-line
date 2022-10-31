import dj_database_url
from decouple import config
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODE = config("MODE", cast=str, default="dev")
SECRET_KEY = config("SECRET_KEY", cast=str)
DEBUG = config("DEBUG", cast=bool, default=True)
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.redirects',
    "index",
    "user",
    'widget_tweaks',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
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

ROOT_URLCONF = 'dhs.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/"templates"],
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

WSGI_APPLICATION = 'dhs.wsgi.application'
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True
STATIC_URL = 'static/'
if MODE == "production":
    STATIC_ROOT = "/home/digiacqo/public_html/static"
else:
    STATIC_ROOT = BASE_DIR/"assets"
STATICFILES_DIRS = [BASE_DIR/"static"]
MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR/"media"
# REGISTRATION-LOGIN URLS
LOGIN_URL = 'account_login'
LOGOUT_URL = 'account_logout'
LOGIN_REDIRECT_URL = 'home'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
)
AUTH_USER_MODEL = 'user.User'
# All Auth SETTINGS
SIGNUP_FORM_CLASS = 'user.forms.CreateUserForm'
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
SOCIALACCOUNT_AUTO_SIGNUP = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_SIGNUP_FORM_CLASS = SIGNUP_FORM_CLASS
ACCOUNT_LOGIN_ON_EMAIL_COMFIRMATION = False
ACCOUNT_PASSWORD_INPUT_RENDER_VALUE = True
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'DHS |'


def ACCOUNT_USER_DISPLAY(user):
    return user.get_full_name()


SITE_ID = 1
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = config("EMAIL_USER")
EMAIL_HOST_PASSWORD = config('EMAIL_PASS')

if MODE == "production":
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_USE_TLS = True
    APPEND_SLASH = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    ADMINS = (
        ("Ineza", "info@digitalhealthline/org"))

    DATABASES = {
        'default': {
            'ENGINE': 'mysql.connector.django',
            'NAME': config("DB_NAME"),
            'USER': config("DB_USER"),
            'PASSWORD': config('DB_PASS'),
            'HOST': '127.0.0.1',
            'PORT': '',
            'OPTIONS': {
                'sql_mode': 'STRICT_TRANS_TABLES',
            }
        }
    }


else:
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


CSRF_TRUSTED_ORIGINS = ["https://*.herokuapp.com",
                        'https://digitalhealthline.org', "http://digitalhealthline.org"]

"""
Django settings for core project.
"""

from pathlib import Path
import os
import sys
import dj_database_url
import cloudinary
import cloudinary.uploader
import cloudinary.api

BASE_DIR = Path(__file__).resolve().parent.parent

# ── LEER EL ARCHIVO .ENV ──
if os.path.exists(os.path.join(BASE_DIR, '.env')):
    with open(os.path.join(BASE_DIR, '.env')) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-tu-clave-local-aqui')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://erp-django-utec-y4xg.onrender.com']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'whitenoise.runserver_nostatic',
    'clientes',
    'proveedores',
    'productos',
    'ventas',
    'reportes',
    'configuracion',
    'catalogo', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'catalogo.context_processors.carrito_info',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3'),
        conn_max_age=600
    )
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'es-mx'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'catalogo' / 'static',
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# WhiteNoise SIN compresión (evita errores de archivos no encontrados)
STATICFILES_STORAGE = 'whitenoise.storage.WhiteNoiseStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SITE_ID = 1
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

LOGIN_REDIRECT_URL = '/productos/'
LOGOUT_REDIRECT_URL = '/'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
}

# ── STRIPE ──
STRIPE_SECRET_KEY      = os.environ.get('STRIPE_SECRET_KEY', 'sk_test_placeholder').strip()
STRIPE_PUBLISHABLE_KEY = os.environ.get('STRIPE_PUBLISHABLE_KEY', 'pk_test_placeholder').strip()
STRIPE_WEBHOOK_SECRET  = os.environ.get('STRIPE_WEBHOOK_SECRET', 'whsec_placeholder').strip()

# ── CLOUDINARY ──
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': 'zl1vxeae',
    'API_KEY': '842798187986568',
    'API_SECRET': 'UH_lKVIztfIuNK34bftnUy3cKTE',
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# ── CELERY (W16) ──
REDIS_URL = os.environ.get('REDIS_URL', '')

if REDIS_URL:
    CELERY_BROKER_URL     = REDIS_URL
    CELERY_RESULT_BACKEND = REDIS_URL
    CELERY_TASK_ALWAYS_EAGER = False
else:
    CELERY_BROKER_URL        = 'memory://'
    CELERY_RESULT_BACKEND    = 'cache+memory://'
    CELERY_TASK_ALWAYS_EAGER = True

CELERY_RESULT_EXPIRES = 3600
CELERY_ACCEPT_CONTENT    = ['json']
CELERY_TASK_SERIALIZER   = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_TASK_SOFT_TIME_LIMIT = 300
CELERY_TASK_TIME_LIMIT       = 360
CELERY_TASK_DEFAULT_QUEUE = 'erp_django'
CELERY_TASK_EAGER_PROPAGATES = True
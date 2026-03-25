from pathlib import Path
import os

with open('.env') as i:
    for line in i:
        key, value = line.strip().split('=', 1)
        os.environ[key] = value

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
RECAPTCHA_SECRET_KEY = os.environ['RECAPTCHA_SECRET_KEY']
WEB3FORMS_ACCESS_KEY = os.environ['WEB3FORMS_ACCESS_KEY']
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
BASE_DIR = Path(__file__).resolve().parent.parent
SITE_ORIGIN = "http://localhost:8000"  
# WEB3FORMS access key is now in .env
# Django secret key is now in .env
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']
# Recaptcha secret key is now in .env
INSTALLED_APPS = [
    'users',
    'chipin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
ROOT_URLCONF = 'ssa_project.urls'
TEMPLATES = [{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'chipin.context_processors.user_profile',
            ],},
},]
WSGI_APPLICATION = 'ssa_project.wsgi.application'
DATABASES = {'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
}}
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
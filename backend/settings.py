import os
from pathlib import Path

import cloudinary

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SK')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
  'elearningplatform.fraanab.repl.co',
]

CSRF_TRUSTED_ORIGINS = [
  'http://127.0.0.1',
  'http://localhost',
  'http://elearningplatform.fraanab.repl.co',
  'https://elearningplatform.fraanab.repl.co'
]

CORS_ALLOW_METHODS = [
  "DELETE",
  "GET",
  "OPTIONS",
  "PATCH",
  "POST",
  "PUT",
]

# Application definition

INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  # 'django_browser_reload',
  'corsheaders',
  'cloudinary',
  # 'cloudinary_storage',
  'core',
  'courses',
]

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  "whitenoise.middleware.WhiteNoiseMiddleware",
  'django.contrib.sessions.middleware.SessionMiddleware',
  "corsheaders.middleware.CorsMiddleware",
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  # "django_browser_reload.middleware.BrowserReloadMiddleware",
]

ROOT_URLCONF = 'backend.urls'

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

WSGI_APPLICATION = 'backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME':
    'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static'

cloudinary.config(
  cloud_name=os.getenv('CCN'),
  api_key=os.getenv('CAK'),
  api_secret=os.getenv('CAS'),
  # secure = true
)

MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STORAGES = {
  "default": {
    "BACKEND": "django.core.files.storage.FileSystemStorage",
  },
  "staticfiles": {
    "BACKEND":
    # "django.contrib.staticfiles.storage.StaticFilesStorage",
    "whitenoise.storage.CompressedManifestStaticFilesStorage",
  }
}

# auth
LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

X_FRAME_OPTIONS = '*'

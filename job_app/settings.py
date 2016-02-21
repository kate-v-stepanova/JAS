"""
Django settings for job_app project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hi!k0n$a0&q$(&1i@uc5#9ymj$vq^6btc)op%@_m81zs*h-udk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

# network, prove, lab, test.for
# research, stand, soft
#
# software - sdn
# prog, software develop
# 2 years - contract limited,
# with_background, 12
# 3 people incl. me;
# 2 years initially;



INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'easy_pdf',
    'job_app',
    'utils',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

ROOT_URLCONF = 'job_app.urls'

WSGI_APPLICATION = 'job_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
APPEND_SLASH = False

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'job_app/static')

TEMPLATE_DIR = os.path.join(BASE_DIR, 'job_app/templates')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'job_app/templates'),
    os.path.join(BASE_DIR, 'job_app/templates', 'CV'),
    os.path.join(BASE_DIR, 'job_app/templates', 'auth'),
)

# TEMPLATES = (
#     os.path.join(BASE_DIR, 'job_app/templates'),
#     os.path.join(BASE_DIR, 'job_app/templates', 'CV'),
#     os.path.join(BASE_DIR, 'job_app/templates', 'auth'),
# )

DEGREE_OPTIONS = (
    ("Bachelor", "Bachelor"),
    ("Specialist", "Specialist"),
)

EMAIL_TEXT = """
Dear {hr_name},
  referring to the Job Position {job_position} published on the webpage: <a href="{job_url}">{job_url}</a>, I'm submitting my application.

  Please find my CV, Motivation Letter and References in the attachment.
  I'm looking forward to hearing from you soon.

  Best regards,
    Ekaterina Stepanova.
"""

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kate.v.stepanova@gmail.com'
EMAIL_HOST_PASSWORD = 'kIx4CheO'
EMAIL_PORT = 587

DATE_FORMAT = '%d.%m.%Y'
USE_L10N = False
DATE_INPUT_FORMATS = [DATE_FORMAT]

# DEFAULT_FROM_EMAIL = 'kate.v.stepanova@gmail.com'
# SERVER_EMAIL = 'kate.v.stepanova@gmail.com'
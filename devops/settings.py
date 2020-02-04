"""
Django settings for devops project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(ku3*yb@g+j6zui0qic2wc4$lmg_fk(e2w$cv#fzrg!5t$@w2d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["192.168.1.67","127.0.0.1"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'dashboard.apps.DashboardConfig',
    'rest_framework',
    'django_filters',
    'idcs.apps.IdcsConfig',
    'users.apps.UsersConfig',
    'cabinet.apps.CabinetConfig',
    'manufacturer.apps.ManufacturerConfig',
    'servers.apps.ServersConfig',
    'rest_framework_swagger'
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

ROOT_URLCONF = 'devops.urls'

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

WSGI_APPLICATION = 'devops.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devops',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '192.168.10.10',
        'OPTIONS': {'init_command':'SET storage_engine=INNODB;',
                    'init_command':"SET sql_mode='STRICT_TRANS_TABLES'",
                    }
    }
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'costom': {
            'format': '%(asctime)s %(name)s %(lineno)s %(levelname)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'costom'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'E:\\pycharmproject\\devops\\devops\\debug.log',
            'maxBytes': 1024 * 1024 * 100,
            'backupCount': 3,
            'formatter': 'costom'
        },
        'request': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'E:\\pycharmproject\\devops\\devops\\request.log',
            # 'when': "D",
            # 'interval':1,
            'formatter': 'costom'
        },
        'server': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'E:\\pycharmproject\\devops\\devops\\server.log',
            # 'when': "D",
            # 'interval': 1,
            'formatter': 'costom'
        },
        'root': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'E:\\pycharmproject\\devops\\devops\\root.log',
            # 'when': "D",
            # 'interval': 1,
            'formatter': 'costom'
        },
        'db_backends': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'E:\\pycharmproject\\devops\\devops\\db_backends.log',
            # 'when': "D",
            # 'interval': 1,
            'formatter': 'costom'
        },
    },
    'loggers': {
        'django': {
            'level': "DEBUG",
            'handlers': ['file'],
            "propagate": True,
        },
        'django.request': {
            'level': "DEBUG",
            'handlers': ['request'],
            "propagate": False,
        },
        'django.server': {
            'level': "DEBUG",
            'handlers': ['server'],
            "propagate": False,
        },
        'django.db.backends': {
            'level': "DEBUG",
            'handlers': ['db_backends'],
            "propagate": False,
        }
    },
    'root':{
        'level':"DEBUG",
        'handlers':["root"]
    }
}

LOGGING= {}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
# REST_FRAMEWORK = {
#     #"DEFAULT_AUTHENTICATION_CLASSES": [],
#     "PAGE_SIZE": 10,
#     #"DEFAULT_PAGINATION_CLASS":"rest_framework.pagination.PageNumberPagination"
#     "DEFAULT_PAGINATION_CLASS":"users.pagination.Pagination",
#     'DEFAULT_FILTER_BACKENDS': (
#         'django_filters.rest_framework.DjangoFilterBackend',
#     ),
#     'DEFAULT_PERMISSION_CLASSES': [
#         'rest_framework.permissions.DjangoObjectPermissions',
#     ],
#     'DEFAULT_PERMISSION_CLASSES': (
#         #'rest_framework.permissions.DjangoModelPermissions',
#         'devops.permissions.Permissions',
#     ),
# }
REST_FRAMEWORK = {
    #分页
    "PAGE_SIZE": 10,
    "DEFAULT_PAGINATION_CLASS":"rest_framework.pagination.PageNumberPagination",
    #搜索
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
    #使用django的模型权限
    'DEFAULT_PERMISSION_CLASSES': (
        #'rest_framework.permissions.DjangoModelPermissions',
        #必须得登录
        'rest_framework.permissions.IsAuthenticated',
        #使用自定义权限
        'devops.permissions.Permissions',
    ),
}
SILENCED_SYSTEM_CHECKS = ['mysql.E001']
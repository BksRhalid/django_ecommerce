from .base import *
import django_heroku
import dj_database_url

DEBUG = False
# ALLOWED_HOSTS = ['*', '127.0.0.1']
ALLOWED_HOSTS = ['soldorak.herokuapp.com']


AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'}
]


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3")
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('DB_USER'),
#         'PASSWORD': config('DB_PASSWORD'),
#         'HOST': config('DB_HOST'),
#         'PORT': ''
#     }
# }

STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')

django_heroku.settings(locals())

# # Static files settings
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(PROJECT_ROOT, 'static_in_env'),
# )

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

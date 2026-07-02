"""Production settings for Akashic Records."""

from decouple import config

from .base import *  # noqa : F403

DEBUG = False

SECRET_KEY = config("SECRET_KEY")  # overrides base just to be explicit

ALLOWED_HOSTS = []

RENDER_EXTERNAL_HOSTNAME = config("RENDER_EXTERNAL_HOSTNAME")

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT"),
        "CONN_MAX_AGE": 600,
        "CONN_HEALTH_CHECKS": True,
        "OPTIONS": {
            "sslmode": "require",
        },
    }
}

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    }
}

INSTALLED_APPS += ["storages"]  # noqa: F405

AWS_ACCESS_KEY_ID = config("SUPABASE_S3_ACCESS_KEY")
AWS_SECRET_ACCESS_KEY = config("SUPABASE_S3_SECRET_KEY")
AWS_STORAGE_BUCKET_NAME = config("SUPABASE_BUCKET_NAME")
AWS_S3_ENDPOINT_URL = config("SUPABASE_S3_ENDPOINT")
AWS_S3_REGION_NAME = config("SUPABASE_S3_REGION")
AWS_S3_ADDRESSING_STYLE = "path"
AWS_QUERYSTRING_AUTH = False

STORAGES["default"] = {"BACKEND": "storages.backends.s3.S3Storage"}  # noqa: F405

MEDIA_URL = config("SUPABASE_MEDIA_URL")

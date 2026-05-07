from .base import *  # noqa : F403


DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",  # noqa : F405
    }
}

INSTALLED_APPS += ["debug_toolbar"]  # noqa : F405

MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa : F405

INTERNAL_IPS = ["127.0.0.1"]

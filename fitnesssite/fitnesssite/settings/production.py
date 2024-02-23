from .base import *

DEBUG = bool(int(os.environ.get("DEBUG",0)))

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

CSRF_TRUSTED_ORIGINS = os.environ.get("CSRF_TRUSTED_ORIGINS").split(" ")

SECRET_KEY = os.environ.get("SECRET_KEY")
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS").split(" ")

CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

try:
    from .local import *
except ImportError:
    pass

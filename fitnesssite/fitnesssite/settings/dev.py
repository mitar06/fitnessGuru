from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-mw&gr*orj_(892bpjrxd@cz(p)nz(9glull(2r&^@e3u4@c@et"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

CSRF_TRUSTED_ORIGINS = ["https://4eb2-89-38-224-204.ngrok-free.app"]

try:
    from .local import *
except ImportError:
    pass

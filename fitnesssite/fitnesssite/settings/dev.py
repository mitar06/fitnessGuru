from .base import *

import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get("SECRET_KEY",'h0u8xvxdj1q0dmtrydwfba#werp#_rdn29+iyo37y7=-nu#3%_')

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR , "media")

INSTALLED_APPS += [
    "debug_toolbar",
]

MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1',
    'https://7a53-31-223-131-172.ngrok-free.app',
    'https://e7fb-31-223-131-172.ngrok-free.app',
]
try:
    from .local import *
except ImportError:
    pass

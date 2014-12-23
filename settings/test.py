from .base import *


'''
Test settings and globals which
allow us to run our test suite
locally.
'''
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}
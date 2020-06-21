from typing import List

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS: List[str] = [
    "rest_framework",
]

LOCAL_APPS = ["users.apps.UsersConfig"]

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = LOCAL_APPS + DJANGO_APPS + THIRD_PARTY_APPS

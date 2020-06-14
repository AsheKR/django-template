# https://docs.djangoproject.com/en/3.0/ref/settings/#std:setting-AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS = [
    "utils.backend.admin_backend.SettingsBackend",
    "django.contrib.auth.backends.ModelBackend",
]

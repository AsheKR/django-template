from os import path

import environ
from config.settings import ROOT_DIR

env = environ.Env()
env.read_env(path.join(ROOT_DIR, "env", ".env.local"))

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env("DEBUG")
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env.str("DJANGO_SECRET_KEY")
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
]

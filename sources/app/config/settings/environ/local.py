from os import path
import environ

env = environ.Env()
env.read_env(path.join(ROOT_DIR, 'env', '.env.local'))

# READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
# if READ_DOT_ENV_FILE:
#     # OS environment variables take precedence over variables from .env
#     env.read_env(path.join(ROOT_DIR, '.env', 'local'))

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env('DEBUG')
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env.str('DJANGO_SECRET_KEY')
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    'localhost',
    '0.0.0.0',
    '127.0.0.1',
]

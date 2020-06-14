from split_settings.tools import optional, include
from os import environ, path
import logging

APP_DIR = path.dirname(path.dirname(path.dirname(__file__)))

logger = logging.getLogger(__name__)

AVAILABLE_DJANGO_ENV = [
    'production',
    'local',
    'test',
]

if not environ.get('DJANGO_ENV'):
    logger.info('DJANGO_ENV not setting. default setting is "local"')

ENV = environ.get('DJANGO_ENV') or 'local'

if ENV not in AVAILABLE_DJANGO_ENV:
    raise ValueError(f'ENV value ({ENV}) is not available value')

if not path.exists(path.join(APP_DIR, 'config', 'settings', ENV)):
    raise FileNotFoundError(f'{path.join(APP_DIR, "config", "settings", ENV)} file (or directory) not found')

include(
    # have order because of dependencies
    'base/apps.py',
    'base/middleware.py',

    # Load all other settings
    'base/*.py',

    # Select the right env:
    f'{ENV}/*.py',
)

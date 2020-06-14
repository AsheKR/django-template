import logging
from os import environ, path

from split_settings.tools import include

APP_DIR = path.dirname(path.dirname(path.dirname(__file__)))
ROOT_DIR = path.dirname(path.dirname(APP_DIR))

logger = logging.getLogger(__name__)

AVAILABLE_DJANGO_ENV = [
    "production",
    "local",
    "test",
]

if not environ.get("DJANGO_ENV"):
    logger.info('DJANGO_ENV not setting. default setting is "local"')

DJANGO_ENV = environ.get("DJANGO_ENV", "local")

if DJANGO_ENV not in AVAILABLE_DJANGO_ENV:
    raise ValueError(f"ENV value ({DJANGO_ENV}) is not available value")

if not path.exists(path.join(APP_DIR, "config", "settings", DJANGO_ENV)):
    raise FileNotFoundError(
        f'{path.join(APP_DIR, "config", "settings", DJANGO_ENV)} file (or directory) not found'
    )

include(
    # have order because of dependencies
    "base/apps.py",
    "base/middleware.py",
    # Load all other settings
    "base/*.py",
    # load django environ
    f"environ/{DJANGO_ENV}.py",
    # Select the right env:
    f"{DJANGO_ENV}/*.py",
)

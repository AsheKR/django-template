import os

from config.settings import APP_DIR

LOCALE_PATHS = (os.path.join(APP_DIR, "config", "locale"),)

# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = "ko-kr"
# https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True
# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

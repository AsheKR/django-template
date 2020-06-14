from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

User = get_user_model()


class SettingsBackend:
    """
    Authenticate against the settings ADMIN_LOGIN and ADMIN_PASSWORD.
    Use the login name and a hash of the password. For example:
    ADMIN_LOGIN = 'admin'
    ADMIN_PASSWORD = 'admin'
    """

    def authenticate(self, username=None, password=None):
        login_valid = settings.ADMIN_LOGIN == username
        pwd_valid = settings.ADMIN_PASSWORD == password
        if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. There's no need to set a password
                # because only the password from settings.py is checked.
                user = User(username=username)
                user.is_staff = True
                user.is_superuser = True
                user.save()
            return user
        return None

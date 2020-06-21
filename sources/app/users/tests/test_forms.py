from django.contrib.auth import get_user_model
from django.test import TestCase
from model_bakery import baker
from users.forms import UserCreationForm

User = get_user_model()


class TestUserCreationForm(TestCase):
    def setUp(self) -> None:
        self.user = baker.prepare(User)

    def test_clean_username(self):
        # A user with proto_user params does not exist yet.
        proto_user = self.user

        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user.password,
                "password2": proto_user.password,
            }
        )

        assert form.is_valid()
        assert form.clean_username() == proto_user.username

        # Creating a user.
        form.save()

        # The user with proto_user params already exists,
        # hence cannot be created.
        form = UserCreationForm(
            {
                "username": proto_user.username,
                "password1": proto_user.password,
                "password2": proto_user.password,
            }
        )

        assert not form.is_valid()
        assert len(form.errors) == 1
        assert "username" in form.errors

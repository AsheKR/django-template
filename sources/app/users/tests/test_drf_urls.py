from django.contrib.auth import get_user_model
from django.urls import resolve, reverse
from model_bakery import baker
from rest_framework.test import APITestCase

User = get_user_model()


class TestDRFUrls(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = baker.make(User)

    def test_user_detail(self):
        assert (
            reverse("api:user-detail", kwargs={"username": self.user.username})
            == f"/api/users/{self.user.username}/"
        )
        assert (
            resolve(f"/api/users/{self.user.username}/").view_name == "api:user-detail"
        )

    def test_user_list(self):
        assert reverse("api:user-list") == "/api/users/"
        assert resolve("/api/users/").view_name == "api:user-list"

    def test_user_me(self):
        assert reverse("api:user-me") == "/api/users/me/"
        assert resolve("/api/users/me/").view_name == "api:user-me"

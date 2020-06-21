from django.contrib.auth import get_user_model
from model_bakery import baker
from rest_framework.test import APIRequestFactory, APITestCase
from users.api.views import UserViewSet

User = get_user_model()


class TestUserViewSet(APITestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.user = baker.make(User)

    def test_get_queryset(self):
        view = UserViewSet()
        request = APIRequestFactory().get("/fake-url/")
        request.user = self.user

        view.request = request

        assert self.user in view.get_queryset()

    def test_me(self):
        view = UserViewSet()
        request = APIRequestFactory().get("/fake-url/")
        request.user = self.user

        view.request = request

        response = view.me(request)

        assert response.data == {
            "username": self.user.username,
            "email": self.user.email,
            "name": self.user.name,
            "url": f"http://testserver/api/users/{self.user.username}/",
        }

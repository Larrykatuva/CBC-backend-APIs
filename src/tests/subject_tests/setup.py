from rest_framework.test import APITestCase
from src.tests.authentication_tests.moc_data import AuthMocs
from src.models.user_models import User
from django.urls import reverse


class TestSetup(APITestCase):

    def login_user(self) -> dict:
        """Login access token method"""
        self.client.post(path=reverse('register-user'),
                         data=AuthMocs().create_user)
        User.objects.filter(
            username=AuthMocs().create_user.get('username')
        ).update(is_verified=True)
        data = self.client.post(
            path=reverse('access-token'),
            data=AuthMocs().login_data
        )
        return data.data.get('tokens')

    def setUp(self) -> None:
        """
        Url configuration
        This method is called in each test.
        """
        self.schools_url = reverse(viewname='schools')
        self.subject_url = reverse(viewname='subjects')
        self.access_token = self.login_user().get('access_token')
        self.auth_headers = {'HTTP_AUTHORIZATION': f'Bearer {self.access_token}'}

        return super().setUp()

    def tearDown(self):
        """
        Deleting all instances created after test has run
        """
        return super().tearDown()


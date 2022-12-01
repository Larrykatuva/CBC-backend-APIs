from src.tests.authentication_tests.setup import TestSetup
from src.tests.authentication_tests.moc_data import AuthMocs
from src.models.user_models import User
import pytest


@pytest.mark.django_db
class TestLoginView(TestSetup):
    """Testing login view"""

    def test_cannot_login_unverified(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        res = self.client.post(path=self.login_url,
                               data=AuthMocs().login_data)
        self.assertEqual(res.status_code, 400)

    def test_cannot_login_with_invalid_details(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        res = self.client.post(path=self.login_url,
                               data=AuthMocs().login_data_invalid)
        self.assertEqual(res.status_code, 400)

    def test_can_login_user(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        User.objects.filter(
            username=AuthMocs().create_user.get('username')
        ).update(is_verified=True)
        res = self.client.post(path=self.login_url,
                               data=AuthMocs().login_data_invalid)
        self.assertEqual(res.status_code, 200)

from src.tests.authentication_tests.setup import TestSetup
from src.tests.authentication_tests.moc_data import AuthMocs
import pytest


@pytest.mark.django_db
class TestRegisterViews(TestSetup):
    """Testing registration view"""

    def test_cannot_register_without_data(self):
        res = self.client.post(path=self.register_url)
        self.assertEqual(res.status_code, 400)

    def test_cannot_register_twice(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        res = self.client.post(path=self.register_url,
                               data=AuthMocs().create_user)
        self.assertEqual(res.status_code, 400)

    def test_can_register_user(self):
        res = self.client.post(path=self.register_url,
                               data=AuthMocs().create_user)
        self.assertEqual(res.status_code, 201)

from src.tests.authentication_tests.setup import TestSetup
from src.tests.authentication_tests.moc_data import AuthMocs
from src.models.user_models import User, ResetCode
import pytest


@pytest.mark.django_db
class TestUserVerification(TestSetup):
    """Testing verification view"""

    def test_cannot_verify_with_wrong_code(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        res = self.client.post(path=self.verify_url,
                               data={'code': "wrong"})
        self.assertEqual(res.status_code, 400)

    def test_can_verify_user(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        user = User.objects.filter(username=AuthMocs().create_user.get('username'))[0]
        code = ResetCode.objects.get(user=user)
        res = self.client.post(path=self.verify_url,
                               data={'code': code.code})
        self.assertEqual(res.status_code, 200)

    def test_can_neglect_wrong_code(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        res = self.client.post(path=self.check_code_url,
                               data={'code': "wrong"})
        self.assertEqual(res.status_code, 400)

    def test_can_check_code(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        user = User.objects.filter(username=AuthMocs().create_user.get('username'))[0]
        code = ResetCode.objects.get(user=user)
        res = self.client.post(path=self.check_code_url,
                               data={'code': code.code})
        self.assertEqual(res.status_code, 200)

    def test_cannot_get_reset_code_with_wrong_email(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        User.objects.filter(
            username=AuthMocs().create_user.get('username')
        ).update(is_verified=True)
        res = self.client.post(path=self.reset_url,
                               data={'email': 'wrong email'})
        self.assertEqual(res.status_code, 400)

    def test_can_get_reset_code(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        User.objects.filter(
            username=AuthMocs().create_user.get('username')
        ).update(is_verified=True)
        res = self.client.post(path=self.reset_url,
                               data={'email': AuthMocs().create_user.get('email')})
        self.assertEqual(res.status_code, 200)

    def test_cannot_reset_password_with_wrong_reset_code(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        User.objects.filter(
            username=AuthMocs().create_user.get('username')
        ).update(is_verified=True)
        self.client.post(path=self.reset_url,
                         data={'email': AuthMocs().create_user.get('email')})
        res = self.client.post(path=self.set_password_url,
                               data={
                                   "code": "wrong",
                                   "password": "qazwsxedc",
                                   "confirm_password": "qazwsxedc"
                               })
        self.assertEqual(res.status_code, 400)

    def test_cannot_reset_password_if_password_is_not_equal_to_confirm_password(self):
        self.client.post(path=self.register_url,
                        data=AuthMocs().create_user)
        User.objects.filter(
            username=AuthMocs().create_user.get('username')
        ).update(is_verified=True)
        self.client.post(path=self.reset_url,
                         data={'email': AuthMocs().create_user.get('email')})
        user = User.objects.filter(username=AuthMocs().create_user.get('username'))[0]
        code = ResetCode.objects.get(user=user)
        res = self.client.post(path=self.set_password_url,
                               data={
                                   "code": code.code,
                                   "password": "qazwsxed",
                                   "confirm_password": "qazwsxedc"
                               })
        self.assertEqual(res.status_code, 400)

    def test_can_reset_password(self):
        self.client.post(path=self.register_url,
                         data=AuthMocs().create_user)
        User.objects.filter(
            username=AuthMocs().create_user.get('username')
        ).update(is_verified=True)
        self.client.post(path=self.reset_url,
                         data={'email': AuthMocs().create_user.get('email')})
        user = User.objects.filter(username=AuthMocs().create_user.get('username'))[0]
        code = ResetCode.objects.get(user=user)
        res = self.client.post(path=self.set_password_url,
                               data={
                                   "code": code.code,
                                   "password": "qazwsxedc",
                                   "confirm_password": "qazwsxedc"
                               })
        self.assertEqual(res.status_code, 200)

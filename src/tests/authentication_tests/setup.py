from rest_framework.test import APITestCase
from django.urls import reverse


class TestSetup(APITestCase):

    def setUp(self) -> None:
        """
        Url configuration
        This method is called in each test.
        """
        self.register_url = reverse(viewname='register-user')
        self.login_url = reverse(viewname='access-token')
        self.verify_url = reverse(viewname='verify-user')
        self.reset_url = reverse(viewname='reset-code')
        self.check_code_url = reverse(viewname='check-code')
        self.set_password_url = reverse(viewname='set-new-password')

        return super().setUp()

    def tearDown(self):
        """
        Deleting all instances created after test has run
        """
        return super().tearDown()

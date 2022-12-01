from src.models import User, ResetCode
from rest_framework import serializers
from src.utils.email import Email
from django.contrib import auth
from rest_framework_simplejwt.tokens import RefreshToken
import string
import random


class UserService:
    """
    Class to handle all user operations.
    """

    @staticmethod
    def register_user(
            email: str,
            username: str,
            phone: str,
            password: str) -> User:
        """Registering new user"""
        return User.objects.create_user(
            username=username,
            email=email,
            phone=phone,
            password=password
        )

    @staticmethod
    def generate_random_code() -> str:
        """Generating a random code for password reset and account activation"""
        return ''.join(random.choices(
            string.ascii_uppercase + string.digits,
            k=6)
        )

    def send_activation_code(self, user: User) -> None:
        """Generating account activation code"""
        code = self.generate_random_code()
        ResetCode.objects.filter(user=user).delete()
        ResetCode.objects.create(
            code=code,
            user=user,
            used=False
        )
        email_subject = 'Verification Code'
        email_body = code + ' is your kurasa verification code.'
        Email.send_mail(
            email_subject=email_subject,
            email_body=email_body,
            send_to=[user.email]
        )

    def send_reset_code(self, user: User) -> None:
        """Generating account password reset code"""
        code = self.generate_random_code()
        ResetCode.objects.filter(user=user).delete()
        ResetCode.objects.create(code=code, user=user, used=False)
        email_subject = 'Password Reset Code'
        email_body = code + ' is your kurasa password code.'
        Email.send_mail(
            email_subject=email_subject,
            email_body=email_body,
            send_to=[user.email]
        )

    @staticmethod
    def get_user_by_code(code: str) -> User:
        """Get user by a reset code"""
        try:
            return ResetCode.objects.get(code=code).user
        except ResetCode.DoesNotExist:
            raise serializers.ValidationError(
                detail={'code': ['Invalid code']},
                code=400
            )

    @staticmethod
    def get_user_by_email(email: str) -> User:
        """Get user by email"""
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user_by_phone(phone: str) -> User:
        """Get user by phone number"""
        try:
            return User.objects.get(phone=phone)
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user_by_username(username: str) -> User:
        """Get user by username"""
        try:
            return User.objects.get(username=username)
        except User.DoesNotExist:
            return None

    @staticmethod
    def confirm_activation_code(code: str, user: User) -> bool:
        """Confirm if activation code is valid"""
        code = ResetCode.objects.filter(code=code, user=user)
        if code.__len__() > 0:
            return True
        return False

    @staticmethod
    def verify_user_account(email: str) -> bool:
        """Activating user account"""
        verify = User.objects.filter(
            email=email
        ).update(is_verified=True)
        ResetCode.objects.filter(user__email=email).delete()
        return verify

    @staticmethod
    def set_new_password(email: str, password: str) -> bool:
        """Setting new user password"""
        user = User.objects.filter(email=email)
        if user.__len__() < 0:
            raise serializers.ValidationError(
                detail={'code': ['User matching ' + email + ' doest not exists']},
                code=400
            )
        user[0].set_password(password)
        user[0].save()
        return True

    @staticmethod
    def authenticate_user(user: User, password: str) -> dict:
        if not user.is_verified:
            raise serializers.ValidationError(
                detail={'email': ['Email ' + user.email + " is not verified"]},
                code=400
            )
        if not user.is_active:
            raise serializers.ValidationError(
                detail={'email': ['Email ' + user.email + " is not active"]},
                code=400
            )
        user = auth.authenticate(email=user.email, password=password)
        if not user:
            raise serializers.ValidationError(
                detail={'password': ['Invalid login details ']},
                code=400
            )
        tokens = RefreshToken.for_user(user)
        kwargs = {'user': user, 'tokens': {
            'refresh_token': str(tokens),
            'access_token': str(tokens.access_token)
        }}
        return kwargs

    @staticmethod
    def update_device_id(email: str, device_id: str) -> None:
        User.objects.filter(email=email).update(device_id=device_id)


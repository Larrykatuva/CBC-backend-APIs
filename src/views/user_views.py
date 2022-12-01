from src.serializers.user_serializers import RegisterUserSerializer, ReadUserSerializer, ResetUserSerializer, \
    CodeResetUserSerializer, NewPasswordUserSerializer, RequestTokenSerializer, LoginResponseSerializer, \
    RequestUserInfoSerialzer
from src.services.user_service import UserService
from src.services.app_service import AppService
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status, serializers
from rest_framework.permissions import IsAuthenticated
import json


class RegisterUserView(CreateAPIView):
    """Register user view"""
    serializer_class = RegisterUserSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = self.user_service.register_user(
            email=data.get('email'),
            username=data.get('username'),
            phone=data.get('phone'),
            password=data.get('password')
        )
        self.user_service.send_activation_code(
            user=user
        )
        return Response(
            data={'message': ['User created and verification code send to your email']},
            status=status.HTTP_201_CREATED
        )


class VerifyUserView(CreateAPIView):
    """Verify user account view"""
    serializer_class = CodeResetUserSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        email = self.user_service.get_user_by_code(
            code=data.get('code')
        )
        verified = self.user_service.verify_user_account(email=email)
        if verified:
            return Response(
                data={'message': ['Account verified successfully']},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                data={'message': ['Account verification failed']},
                status=status.HTTP_400_BAD_REQUEST
            )


class RequestResetCodeView(CreateAPIView):
    """Request password reset code"""
    serializer_class = ResetUserSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = self.user_service.get_user_by_email(
            email=data.get('email')
        )
        if not user:
            raise serializers.ValidationError(
                detail={'email': [data.get('email') + " email does not exist"]},
                code=400
            )
        self.user_service.send_reset_code(user=user)
        return Response(
            data={'message': ['Password reset code send to email.']},
            status=status.HTTP_200_OK
        )


class CheckResetCode(CreateAPIView):
    serializer_class = CodeResetUserSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        email = self.user_service.get_user_by_code(
            code=data.get('code')
        )
        return Response(
            data={'message': ['Code accepted, set your new password',
                              {'email': email.__str__()}]
                  },
            status=status.HTTP_200_OK
        )


class SetPasswordView(CreateAPIView):
    serializer_class = NewPasswordUserSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        email = self.user_service.get_user_by_code(
            code=data.get('code')
        )
        self.user_service.set_new_password(
            email=email.__str__(),
            password=data.get('password')
        )
        return Response(
            data={'message': ['Password updated successfully']},
            status=status.HTTP_200_OK
        )


class AccessTokenView(CreateAPIView):
    serializer_class = RequestTokenSerializer
    user_service = UserService()

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = self.user_service.get_user_by_username(username=data.get('username'))
        if not user:
            raise serializers.ValidationError(
                detail={'email': ["Username does not exist"]},
                code=400
            )
        tokens = self.user_service.authenticate_user(
            user=user,
            password=data.get('password')
        )
        if data.get('device_id'):
            self.user_service.update_device_id(
                email=user.email,
                device_id=data.get('device_id')
            )
        self.serializer_class = LoginResponseSerializer
        serialized_data = self.serializer_class(tokens)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_200_OK
        )


class UserInfoView(CreateAPIView):
    serializer_class = RequestUserInfoSerialzer
    app_service = AppService()

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        if not self.app_service.get_app_by_client_id(
                client_id=data.get('client_id')
        ):
            raise serializers.ValidationError(
                detail={'client_id': ["Invalid client_id"]},
                code=400
            )
        if not self.app_service.get_app_by_client_secret(
                client_secret=data.get('client_secret')
        ):
            raise serializers.ValidationError(
                detail={'client_secret': ["Invalid client_secret"]},
                code=400
            )
        self.serializer_class = ReadUserSerializer
        serialized_data = self.serializer_class(request.user)
        return Response(
            data=serialized_data.data,
            status=status.HTTP_200_OK
        )


class IntrospectView(CreateAPIView):
    serializer_class = RequestUserInfoSerialzer
    app_service = AppService()

    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        if not self.app_service.get_app_by_client_id(
                client_id=data.get('client_id')
        ):
            raise serializers.ValidationError(
                detail={'client_id': ["Invalid client_id"]},
                code=400
            )
        if not self.app_service.get_app_by_client_secret(
                client_secret=data.get('client_secret')
        ):
            raise serializers.ValidationError(
                detail={'client_secret': ["Invalid client_secret"]},
                code=400
            )
        return Response(
            data={'status': True},
            status=status.HTTP_200_OK
        )

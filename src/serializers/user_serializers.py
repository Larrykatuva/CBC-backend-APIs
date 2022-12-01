from src.models import User
from rest_framework import serializers


class RegisterUserSerializer(serializers.ModelSerializer):
    """Register user serializer for new user registration"""

    class Meta:
        model = User
        fields = ('email', 'username', 'phone', 'password')


class LoginUserSerializer(serializers.ModelSerializer):
    """Login serializer for user login"""

    class Meta:
        model = User
        fields = ('username', 'password')


class ResetUserSerializer(serializers.Serializer):
    """Reset user serializer for resetting user password"""
    email = serializers.EmailField(required=True, max_length=256)

    class Meta:
        fields = ('email',)


class CodeResetUserSerializer(serializers.Serializer):
    """Reset code serializer for resetting user password"""

    code = serializers.CharField(max_length=6, min_length=6)

    class Meta:
        fields = ('code',)


class NewPasswordUserSerializer(serializers.Serializer):
    """New password serializer for setting new user password"""
    code = serializers.CharField(max_length=6, min_length=6)
    password = serializers.CharField(max_length=256, min_length=8)
    confirm_password = serializers.CharField(max_length=256, min_length=8)

    class Meta:
        fields = ('password', 'confirm_password', 'code')

    def validate(self, attrs):
        password = attrs.get('password', '')
        confirm_password = attrs.get('confirm_password', '')
        if password.__ne__(confirm_password):
            raise serializers.ValidationError(detail='Password should match confirm password', code=400)

        return attrs


class RequestTokenSerializer(serializers.Serializer):
    """Request access token serializer"""
    username = serializers.CharField(max_length=256, required=True)
    password = serializers.CharField(max_length=256, required=True)
    device_id = serializers.CharField(max_length=2000, required=False)

    class Meta:
        model = User
        fields = ('username', 'password', 'device_id')


class ResponseTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=2000)
    access_token = serializers.CharField(max_length=2000)

    class Meta:
        fields = ('refresh_token', 'access_token')


class RequestUserInfoSerialzer(serializers.Serializer):
    client_id = serializers.CharField(max_length=256, required=True)
    client_secret = serializers.CharField(max_length=256, required=True)

    class Meta:
        fields = ('client_id', 'client_secret')


class ReadUserSerializer(serializers.ModelSerializer):
    """Read user serializer for get methods"""

    class Meta:
        model = User
        exclude = ('password',)


class LoginResponseSerializer(serializers.Serializer):
    user = ReadUserSerializer()
    tokens = ResponseTokenSerializer()

    class Meta:
        fields = ('user', 'tokens',)

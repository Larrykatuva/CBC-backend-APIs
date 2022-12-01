from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.db.models.deletion import CASCADE
from src.models.server_models import App
import uuid


class UserManager(BaseUserManager):
    """Customizing default user model to override some creation features"""
    def create_user(self, username, email, phone, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if email is None:
            raise TypeError('Users should have a email')
        if phone is None:
            raise TypeError('Users should have a phone')
        user = self.model(username=username, email=self.normalize_email(email), phone=phone)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, phone, password=None):
        if username is None:
            raise TypeError('Users should have a username')
        if password is None:
            raise TypeError('Users should have a password')
        if email is None:
            raise TypeError('Users should have a email')
        if phone is None:
            raise TypeError('Users should have a phone')
        user = self.create_user(username, email, password, phone)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User model representation"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    phone = models.CharField(max_length=13, unique=True)
    device_id = models.CharField(max_length=2000, null=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    if_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()


class ResetCode(models.Model):
    """Reset password model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=CASCADE)
    code = models.CharField(max_length=10)
    used = models.BooleanField(max_length=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AuthCode(models.Model):
    """Authentication code model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, to_field='id', on_delete=CASCADE)
    app = models.ForeignKey(App, to_field='id', on_delete=CASCADE)
    code = models.CharField(max_length=256)
    redeemed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



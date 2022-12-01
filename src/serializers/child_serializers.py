from src.models.user_models import User
from src.models.school_models import Child, ChildInstance
from rest_framework import serializers


class CreateChildSerializer(serializers.ModelSerializer):
    """Create child serializer data schema"""
    class Meta:
        model = Child
        fields = ('fullname', 'dob')


class UpdateChildSerializer(serializers.ModelSerializer):
    """Update child serializer data schema"""
    class Meta:
        model = Child
        fields = ('fullname', 'dob')


class UserSerializer(serializers.ModelSerializer):
    """User serializer data schema to be nested in child serializer schemas"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')


class ChildInstanceSerializer(serializers.ModelSerializer):
    """Child instance serializer to be nested in child serializer schema"""
    class Meta:
        model = ChildInstance
        fields = ('id', 'grade')


class ReadChildSerializer(serializers.ModelSerializer):
    """Read child serializer schema"""
    parent = UserSerializer()
    child_instances = ChildInstanceSerializer(many=True)

    class Meta:
        model = Child
        fields = ('id', 'fullname', 'dob', 'created_at', 'updated_at', 'parent', 'child_instances')

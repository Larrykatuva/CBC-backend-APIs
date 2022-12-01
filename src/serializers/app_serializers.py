from src.models import App
from rest_framework import serializers


class CreateAppSerializer(serializers.ModelSerializer):
    """Create app serializer for post method"""
    redirect_url = serializers.URLField(required=True, max_length=256)

    class Meta:
        model = App
        fields = ('name', 'manager', 'redirect_url')


class UpdateAppSerializer(serializers.Serializer):
    """Update serializer for patch and put request methods"""

    name = serializers.CharField(max_length=256, required=False)
    manager = serializers.CharField(max_length=256, required=False)
    is_active = serializers.CharField(required=False)
    redirect_url = serializers.URLField(required=True, max_length=256)

    class Meta:
        fields = ('name', 'manager', 'is_active', 'redirect_url')


class ReadAppSerializer(serializers.ModelSerializer):
    """Read serializer for get methods"""

    class Meta:
        model = App
        fields = '__all__'


class ManagerSerializer(serializers.ModelSerializer):
    """Manager field serializer"""

    class Meta:
        model = App
        fields = ('manager',)

from src.models import ChildInstance, GeneratedFile
from rest_framework import serializers


class CreateReportSerializer(serializers.ModelSerializer):
    """Create report serializer"""
    class Meta:
        model = GeneratedFile
        fields = ('filename', 'url', 'child_instance')


class ReportChildInstanceSerializer(serializers.ModelSerializer):
    """Child instance serializer schema to be nested report serializer"""
    class Meta:
        model = ChildInstance
        fields = '__all__'


class ReadReportSerializer(serializers.ModelSerializer):
    """Read report serializer"""
    child_instance = ReportChildInstanceSerializer()

    class Meta:
        model = GeneratedFile
        fields = ('id', 'filename', 'url', 'downloaded', 'created_at',
                  'updated_at', 'child_instance')

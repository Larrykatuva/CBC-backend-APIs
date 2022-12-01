from src.models.school_models import School
from rest_framework import serializers
from src.services.school_service import SchoolService


class CreateSchoolSerializer(serializers.ModelSerializer):
    """Create school serializer data schema"""

    class Meta:
        model = School
        fields = ('name', 'location', 'address', 'telephone',
                  'motto', 'status', 'logo')

    def validate(self, attrs):
        """Custom serializer validation"""
        name = attrs.get('', 'name')
        if SchoolService.get_school_by_name(name=name):
            raise serializers.ValidationError(
                detail={'name': [name + " school name already exists"]},
                code=400
            )
        return attrs


class ReadSchoolSerializer(serializers.ModelSerializer):
    """Read school serializer data schema"""

    class Meta:
        model = School
        fields = '__all__'


class UpdateSchoolSerializer(serializers.ModelSerializer):
    """Update school serializer data schema"""

    class Meta:
        model = School
        fields = ('name', 'location', 'address', 'telephone',
                  'motto', 'logo')

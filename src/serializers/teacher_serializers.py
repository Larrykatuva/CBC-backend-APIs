from src.models.school_models import School, Teacher
from rest_framework import serializers
from src.services.teacher_service import TeacherService


class CreateTeacherSerializer(serializers.ModelSerializer):
    """Create teacher serializer data schema"""
    class Meta:
        model = Teacher
        fields = ('fullname', 'phone', 'email', 'school', 'school',
                  'id_number', 'tsc_number', 'surname', 'other_names')

    def validate(self, attrs):
        """Custom serializer validation"""
        id_number = attrs.get('', 'id_number')
        tsc_number = attrs.get('', 'tsc_number')
        if TeacherService.filter_teachers({'id_number': id_number}).__len__() > 0:
            raise serializers.ValidationError(
                detail={'id_number': ['Teacher with ' + id_number + 'already exists']},
                code=400
            )
        if TeacherService.filter_teachers({'tsc_number': tsc_number}).__len__() > 0:
            raise serializers.ValidationError(
                detail={'tsc_number': ['Teacher with ' + tsc_number + 'already exists']},
                code=400
            )
        return attrs


class UpdateTeacherSerializer(serializers.ModelSerializer):
    """Update teacher serializer data schema"""
    class Meta:
        model = Teacher
        fields = ('fullname', 'phone', 'email', 'school', 'school',
                  'id_number', 'tsc_number', 'surname', 'other_names')


class SchoolSerializer(serializers.ModelSerializer):
    """Read school serializer schema to be nested in teacher read serializer schemas """
    class Meta:
        model = School
        fields = '__all__'


class ReadTeacherSerializer(serializers.ModelSerializer):
    """Teacher read serializer schema"""
    school = SchoolSerializer()

    class Meta:
        model = Teacher
        fields = ('id', 'fullname', 'phone', 'email', 'school', 'school', 'id_number',
                  'tsc_number', 'surname', 'other_names', 'created_at', 'updated_at')


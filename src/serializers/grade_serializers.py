from src.models.school_models import Grade, Teacher, School
from src.services.grade_service import GradeService
from rest_framework import serializers


class CreateGradeSerializer(serializers.ModelSerializer):
    """Create grade serializer data schema"""
    class Meta:
        model = Grade
        fields = ('name', 'grade', 'school', 'status', 'class_number', 'teacher')

    def validate(self, attrs):
        """Custom serializer validation"""
        school = attrs.get('school')
        class_number = attrs.get('class_number')

        if GradeService.filter_grades(
                {'school': school, 'class_number': class_number}
        ).__len__() > 0:
            raise serializers.ValidationError(
                detail={'grade': ['Grade already exist']},
                code=400
            )
        return attrs


class UpdateGradeSerializer(serializers.ModelSerializer):
    """Update grade serializer data schema"""
    class Meta:
        model = Grade
        fields = ('name', 'grade', 'school', 'status', 'class_number', 'teacher')

    def validate(self, attrs):
        """Custom serializer validation"""
        school = attrs.get('school')
        class_number = attrs.get('class_number')

        if GradeService.filter_grades(
                {'school': school, 'class_number': class_number}
        ).__len__() > 0:
            raise serializers.ValidationError(
                detail={'grade': ['Grade already exist']},
                code=400
            )
        return attrs


class TeacherSerializer(serializers.ModelSerializer):
    """Teacher serializer data schema to be nested in grade serializers"""
    class Meta:
        model = Teacher
        fields = ('id', 'fullname', 'phone', 'email', 'status', 'surname')


class SchoolSerializer(serializers.ModelSerializer):
    """School serializer data schema to be nested in grade serializers"""
    class Meta:
        model = School
        fields = '__all__'


class ReadGradeSerializer(serializers.ModelSerializer):
    """Read serializer data schema"""
    teacher = TeacherSerializer()
    school = SchoolSerializer()

    class Meta:
        model = Grade
        fields = ('id', 'name', 'grade', 'status', 'created_at', 'updated_at',
                  'teacher', 'school')

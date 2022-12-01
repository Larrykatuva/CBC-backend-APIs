from src.models.school_models import Subject, School
from src.services.subject_service import SubjectService
from rest_framework import serializers


class CreateSubjectSerializer(serializers.ModelSerializer):
    """Create subject serializer data schema"""
    class Meta:
        model = Subject
        fields = ('subject_title', 'status', 'course', 'color',
                  'school', 'abbreviation')

    def validate(self, attrs):
        """Custom serializer validation"""
        school = attrs.get('school')
        subject_title = attrs.get('subject_title')

        if SubjectService.filter_subjects(
                {'school': school, 'subject_title': subject_title}
        ).__len__() > 0:
            raise serializers.ValidationError(
                detail={'subject': ['Subject already exist']},
                code=400
            )
        return attrs


class UpdateSubjectSerializer(serializers.ModelSerializer):
    """Update subject serializer data schema"""
    class Meta:
        model = Subject
        fields = ('subject_title', 'status', 'course', 'course',
                  'school', 'abbreviation')


class SchoolSerializer(serializers.ModelSerializer):
    """School serializer schema to be nested in subject serializers"""
    class Meta:
        model = School
        fields = '__all__'


class ReadSubjectSerializer(serializers.ModelSerializer):
    """Read school serializer data schema"""
    school = SchoolSerializer()

    class Meta:
        model = Subject
        fields = ('id', 'subject_title', 'status', 'course', 'color',
                  'abbreviation', 'school')



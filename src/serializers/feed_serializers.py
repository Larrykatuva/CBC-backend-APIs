from src.models.school_models import Feed, Teacher, ChildInstance, Grade, Child, Comment
from rest_framework import serializers


class CreateFeedSerializer(serializers.ModelSerializer):
    """Create feed serializer data schema"""
    class Meta:
        model = Feed
        fields = ('teacher', 'learning_area', 'strand', 'substrand', 'indicator',
                  'assessment_type', 'assessment_description', 'assessment_score',
                  'assessment_comment', 'learning_outcome', 'child_instance')


class UpdateFeedSerializer(serializers.ModelSerializer):
    """Update feed serializer data schema"""
    class Meta:
        model = Feed
        fields = ('teacher', 'learning_area', 'strand', 'substrand', 'indicator',
                  'assessment_type', 'assessment_description', 'assessment_score',
                  'assessment_comment', 'learning_outcome', 'child_instance')


class ChildSerializer(serializers.ModelSerializer):
    """Child serializer to be nested in feed serializers"""
    class Meta:
        model = Child
        fields = '__all__'


class GradeSerializer(serializers.ModelSerializer):
    """Grade serializer to be nested in feed serializer"""
    class Meta:
        model = Grade
        fields = '__all__'


class ChildInstanceSerializer(serializers.ModelSerializer):
    """Child instance serializer to be nested in feed serializers"""
    child = ChildSerializer()
    grade = GradeSerializer()

    class Meta:
        model = ChildSerializer
        fields = ('id', 'created_at', 'updated_at', 'child', 'grade')


class TeacherSerializer(serializers.ModelSerializer):
    """Teacher serializer data schema to be nested in feed serializers"""
    class Meta:
        model = Teacher
        fields = ('id', 'fullname', 'phone', 'email', 'status', 'surname')


class FeedCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class ReadFeeSerializer(serializers.ModelSerializer):
    """Read feed serializer data schema"""
    teacher = TeacherSerializer()
    child_instance = ChildInstance()
    comment_feeds__count = serializers.IntegerField(allow_null=True)

    class Meta:
        model = Feed
        fields = ('id', 'learning_area', 'strand', 'substrand', 'indicator',
                  'assessment_type', 'assessment_description', 'assessment_score',
                  'assessment_comment', 'learning_outcome', 'assessment_at',
                  'created_at', 'teacher', 'child_instance', 'comment_feeds__count')


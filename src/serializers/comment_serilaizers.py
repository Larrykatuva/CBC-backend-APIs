from src.models.school_models import Comment, Feed, Teacher
from src.models.user_models import User
from rest_framework import serializers


class CreatCommentSerializer(serializers.ModelSerializer):
    """Create comment serializer data schema"""
    class Meta:
        model = Comment
        fields = ('feed', 'reactions', 'text', 'seen')


class UpdateCommentSerializer(serializers.ModelSerializer):
    """Create comment serializer data schema"""
    class Meta:
        model = Comment
        fields = ('feed', 'comment_user', 'reactions', 'text', 'seen')


class UserSerializer(serializers.ModelSerializer):
    """User serializer data schema to be nested in comment serializer schemas"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone')


class TeacherSerializerSchema(serializers.ModelSerializer):
    """Teacher serializer data schema to be nested in comment serializer schemas"""
    class Meta:
        model = Teacher
        fields = '__all__'


class FeedSerializer(serializers.ModelSerializer):
    """Feed serializer data schema to be nested in comment serializer schemas"""
    teacher = TeacherSerializerSchema()

    class Meta:
        model = Feed
        fields = ('id', 'learning_area', 'strand', 'substrand', 'indicator',
                  'assessment_type', 'assessment_description', 'assessment_score',
                  'assessment_comment', 'learning_outcome', 'child_instance',
                  'assessment_at', 'created_at', 'teacher')


class ReadCommentSerializer(serializers.ModelSerializer):
    """"Read comment serializer data schema"""
    feed = FeedSerializer()
    comment_user = UserSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'reactions', 'text', 'seen', 'created_at', 'updated_at',
                  'feed', 'comment_user')



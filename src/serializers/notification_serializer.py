from src.models.school_models import Notification, Feed, Comment, Teacher, ChildInstance
from rest_framework import serializers


class NotificationTeacherSerializer(serializers.ModelSerializer):
    """Teacher serializer to be nested in notification serializer"""
    class Meta:
        model = Teacher
        fields = '__all__'


class NotificationChildInstanceSerializer(serializers.ModelSerializer):
    """Child instance serializer to be nested in notification serializer"""
    class Meta:
        model = ChildInstance
        field = "__all__"


class NotificationFeedSerializer(serializers.ModelSerializer):
    """Feed serializer to be nested in notification serializer"""
    class Meta:
        model = Feed
        fields = '__all__'


class NotificationCommentSerializer(serializers.ModelSerializer):
    """Comment serializer to be nested in notification serializer"""
    class Meta:
        model = Comment
        fields = '__all__'


class NotificationSerializer(serializers.ModelSerializer):
    """Notification serializer"""
    comment = NotificationCommentSerializer()
    feed = NotificationFeedSerializer()

    class Meta:
        model = Notification
        fields = ('id', 'parent', 'body', 'title', 'type', 'created_at',
                  'updated_at', 'comment', 'feed')





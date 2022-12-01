from django.db import models
import uuid

from django.db.models import CASCADE, DO_NOTHING
from src.models.user_models import User


class School(models.Model):
    """School model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    location = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    telephone = models.CharField(max_length=13)
    motto = models.TextField()
    status = models.SmallIntegerField(default=0)
    logo = models.FileField(upload_to='logos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Teacher(models.Model):
    """Teacher model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fullname = models.CharField(max_length=256)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=256)
    status = models.SmallIntegerField(default=0)
    school = models.ForeignKey(to=School, to_field='id', related_name='school_teachers', on_delete=CASCADE)
    id_number = models.CharField(max_length=50)
    tsc_number = models.CharField(max_length=50)
    surname = models.CharField(max_length=256)
    other_names = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Child(models.Model):
    """Child model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(to=User, to_field='id', related_name='parent_children', on_delete=CASCADE)
    fullname = models.CharField(max_length=256)
    dob = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Grade(models.Model):
    """Grade model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256)
    grade = models.CharField(max_length=256)
    school = models.ForeignKey(to=School, to_field='id', related_name='school_grades', on_delete=CASCADE)
    status = models.BooleanField(default=False)
    class_number = models.IntegerField()
    teacher = models.ForeignKey(to=Teacher, to_field='id', related_name='class_teachers', on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ChildInstance(models.Model):
    """Child instance model to link child with the grandes are in"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    child = models.ForeignKey(to=Child, to_field='id', related_name='child_instances', on_delete=DO_NOTHING)
    grade = models.ForeignKey(to=Grade, to_field='id', related_name='instance_grades', on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Subject(models.Model):
    """Subject model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject_title = models.CharField(max_length=100)
    status = models.SmallIntegerField(default=0)
    course = models.CharField(max_length=256)
    color = models.CharField(max_length=50)
    school = models.ForeignKey(to=School, to_field='id', related_name='school_subjects', on_delete=CASCADE)
    abbreviation = models.CharField(max_length=256)


class Feed(models.Model):
    """Feed model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    teacher = models.ForeignKey(to=Teacher, to_field='id', related_name='teacher_feeds', on_delete=DO_NOTHING)
    learning_area = models.TextField()
    strand = models.CharField(max_length=256)
    substrand = models.CharField(max_length=256)
    indicator = models.CharField(max_length=256)
    assessment_type = models.CharField(default='formative', max_length=256)
    assessment_description = models.TextField()
    assessment_score = models.IntegerField()
    assessment_comment = models.TextField()
    learning_outcome = models.TextField()
    child_instance = models.ForeignKey(to=ChildInstance, to_field='id', related_name='child_instance_feeds',
                                       on_delete=DO_NOTHING)
    assessment_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    """Comment model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    feed = models.ForeignKey(to=Feed, to_field='id', related_name='comment_feeds', on_delete=CASCADE)
    comment_user = models.ForeignKey(to=User, to_field='id', related_name='user_comments', on_delete=CASCADE)
    reactions = models.IntegerField()
    text = models.TextField()
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Notification(models.Model):
    """Notifications model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    feed = models.ForeignKey(to=Feed, to_field='id', related_name='feed_notifications', on_delete=CASCADE, null=True)
    comment = models.ForeignKey(to=Comment, to_field='id', related_name='comment_notifications', on_delete=CASCADE,
                                null=True)
    parent = models.ForeignKey(to=User, to_field='id', related_name='parent_notifications', on_delete=CASCADE, null=True)
    body = models.TextField()
    title = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class GeneratedFile(models.Model):
    """Generated files model"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    filename = models.CharField(max_length=256)
    url = models.URLField(max_length=1000)
    downloaded = models.BooleanField(default=False)
    child_instance = models.ForeignKey(to=ChildInstance, to_field='id', related_name='child_instance_files',
                                       on_delete=DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


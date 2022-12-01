# Generated by Django 4.0.2 on 2022-09-03 08:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0009_delete_comment_delete_feed_delete_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=256)),
                ('dob', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parent_children', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ChildInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_instances', to='src.child')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=256)),
                ('telephone', models.CharField(max_length=13)),
                ('motto', models.TextField()),
                ('status', models.SmallIntegerField(default=0)),
                ('logo', models.FileField(upload_to='logos/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=13)),
                ('email', models.EmailField(max_length=256)),
                ('status', models.SmallIntegerField(default=0)),
                ('id_number', models.CharField(max_length=50)),
                ('tsc_number', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=256)),
                ('other_names', models.CharField(max_length=256)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_teachers', to='src.school')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('subject_title', models.CharField(max_length=100)),
                ('status', models.SmallIntegerField(default=0)),
                ('course', models.CharField(max_length=256)),
                ('color', models.CharField(max_length=50)),
                ('abbreviation', models.CharField(max_length=256)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_subjects', to='src.school')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('grade', models.CharField(max_length=256)),
                ('status', models.BooleanField(default=False)),
                ('class_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='school_grades', to='src.school')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='class_teachers', to='src.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('learning_area', models.TextField()),
                ('strand', models.CharField(max_length=256)),
                ('substrand', models.CharField(max_length=256)),
                ('indicator', models.CharField(max_length=256)),
                ('assessment_type', models.CharField(default='formative', max_length=256)),
                ('assessment_description', models.TextField()),
                ('assessment_score', models.IntegerField()),
                ('assessment_comment', models.TextField()),
                ('learning_outcome', models.TextField()),
                ('assessment_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('child_instance', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='child_instance_feeds', to='src.childinstance')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='teacher_feeds', to='src.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reactions', models.IntegerField()),
                ('text', models.TextField()),
                ('seen', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL)),
                ('feed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_feeds', to='src.feed')),
            ],
        ),
        migrations.AddField(
            model_name='childinstance',
            name='grade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='instance_grades', to='src.grade'),
        ),
    ]

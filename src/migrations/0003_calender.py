# Generated by Django 4.0.2 on 2022-08-24 18:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_app_redirect_url_authcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=256)),
                ('description', models.CharField(max_length=256)),
                ('fromTimestamp', models.IntegerField()),
                ('toTimestamp', models.IntegerField()),
            ],
        ),
    ]

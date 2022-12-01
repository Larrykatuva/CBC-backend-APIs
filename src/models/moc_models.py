from django.db import models
import uuid


class Calender(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    fromTimestamp = models.IntegerField()
    toTimestamp = models.IntegerField()


class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parentId = models.CharField(max_length=256)
    feedbackType = models.CharField(max_length=256)
    feedbackDescription = models.CharField(max_length=256)


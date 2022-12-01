from django.db import models
from django.db.models.deletion import CASCADE
import uuid


class App(models.Model):
    """Models representation of apps registered in the system."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=256, unique=True)
    manager = models.CharField(max_length=256)
    client_id = models.CharField(max_length=256, unique=True)
    client_secret = models.CharField(max_length=256, unique=True)
    redirect_url = models.CharField(max_length=245, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


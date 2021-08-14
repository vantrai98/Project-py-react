from django.contrib.auth.models import User
from django.db import models

PROJECT_STATUS = [
    ('C', 'Complete'),
    ('D', 'Doing'),
    ('R', 'Cancel'),
]


class Project(models.Model):
    code = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=250, blank=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    status = models.CharField(
        max_length=15, default="D", choices=PROJECT_STATUS)
    creator = models.ForeignKey(
        to=User, related_name='projects', on_delete=models.CASCADE, null=True)

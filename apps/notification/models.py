from django.db import models
from django.contrib.auth.models import User


class Notification(models.Model):
    name = models.CharField(max_length=30)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.name

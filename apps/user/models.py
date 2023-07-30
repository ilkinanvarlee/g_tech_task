from django.db import models
from django.contrib.auth.models import User
from apps.web.models import TimeStamp


class Profile(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', editable=False)
    bio = models.TextField(null=True)
    present_work_space = models.CharField(max_length=100, null=True)
    live_country = models.CharField(max_length=30, null=True)
    gender = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username

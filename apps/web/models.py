from django.db import models
from django.contrib.auth.models import User


class TimeStamp(models.Model):
    """
    This is custom timestamp model :
        For inheritance to all model
    """

    created = models.DateTimeField('created at', auto_now_add=True)
    updated = models.DateTimeField('updated at', auto_now=True)

    class Meta:
        abstract = True


class Product(models.Model):
    user = models.ManyToManyField(User, related_name='product')
    name = models.CharField(max_length=50)
    price = models.IntegerField()

    def __str__(self):
        return self.name

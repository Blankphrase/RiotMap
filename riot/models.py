from  django.contrib.auth.models import User
from django.contrib.gis.db import models

# Create your models here.

class Places(models.Model):
    """
    Model for an important place
    """
    name = models.CharField(max_length=200)
    location = models.PointField()


class Important(models.Model):
    """
    Model for an event
    """
    name = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    place = models.ForeignKey(Places)




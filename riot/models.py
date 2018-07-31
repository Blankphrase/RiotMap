from  django.contrib.auth.models import User
from django.contrib.gis.db import models

# Create your models here.

class Places(models.Model):
    """
    Model for an important place
    """
    name = models.CharField(max_length=200)
    location = models.PointField()


class Profile(models.Model):
    """
    Model for an important place
    """
    user = models.OneToOneField(User)
    locationName = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    place = models.ForeignKey(Places)

class RiotPronePlaces(models.Model):
    """
    Model for an area where riot has occured
    """
    name = models.CharField(max_length=200)
    riotProne = models.ForeignKey(Places)

class NowRioting(models.Model):
    """
    Model for an area where a riot is happening
    """
    name = models.CharField(max_length=200)
    riotingNow = models.ForeignKey(Places)


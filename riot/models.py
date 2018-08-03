from  django.contrib.auth.models import User
from django.contrib.gis.db import models

# Create your models here.

class Places(models.Model):
    """
    Model for an important place
    """
    name = models.CharField(max_length=200)
    location = models.PointField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    """
    Model for an important place
    """
    user = models.OneToOneField(User)
    datetime = models.DateTimeField()
    place = models.ForeignKey(Places, blank=True)


    def __str__(self):
        return "%s" % (self.place.name)



class RiotPronePlaces(models.Model):
    """
    Model for an area where riot has occured
    """
    place = models.ForeignKey(Places)


    def __str__(self):
        return "%s" % (self.place.name)



class NowRioting(models.Model):
    """
    Model for an area where a riot is happening
    """
    place = models.ForeignKey(Places)

    def __str__(self):
        return "%s" % (self.place.name)



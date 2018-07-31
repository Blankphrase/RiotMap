from django.db import models

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length = 30)
    email = models.EmailField()
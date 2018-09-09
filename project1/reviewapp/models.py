from django.db import models
from django.contrib.auth.models import User

class checkin(models.Model):
    address = models.CharField(max_length=100)
    longitude = models.CharField(max_length=50)
    latitude = models.CharField(max_length=50)
    place_name = models.CharField(max_length=50)
    review = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



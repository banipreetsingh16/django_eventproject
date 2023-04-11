from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile 

# Create your models here.

class Events(models.Model):
    event_name=models.CharField(max_length=100)
    description = models.TextField()
    starts_at=models.IntegerField()
    ends_at=models.IntegerField()
    last_event=models.CharField(max_length=100)
    upcoming_event=models.CharField(max_length=100)

class Participants(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    event_name=models.ForeignKey(Events, on_delete=models.CASCADE)
    is_registered=models.BooleanField(default=False)
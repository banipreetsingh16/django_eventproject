from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile 

# Create your models here.

class Events(models.Model):
    event_name=models.CharField(max_length=100)
    description = models.TextField()
    starts_at=models.DateTimeField()
    ends_at=models.DateTimeField()
    venue=models.CharField()


class Participants(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    event_name=models.ForeignKey(Events, on_delete=models.CASCADE)
    is_registered=models.BooleanField(default=False)

    class Meta:
        default_related_name = 'participants'
    def __str__(self):
        return self.user.username
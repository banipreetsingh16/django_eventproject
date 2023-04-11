from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    email=models.EmailField(max_length=254,unique=True)
    age=models.IntegerField()
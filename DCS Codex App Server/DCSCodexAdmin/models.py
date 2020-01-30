from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     email = models.EmailField(unique=True)

class Group(models.Model):
     name = models.CharField(max_length=50)

class Entry(models.Model):
     date = models.DateField()
     name = models.CharField(max_length=50)
     info = models.TextField(max_length=250)
     group = models.ForeignKey('Group', on_delete=models.CASCADE)

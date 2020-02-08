'''
This is a course requirement for CS 192 Software Engineering II under the supervision of Asst. Prof. Ma. Rowena C. Solamo 
of the Department of Computer Science, College of Engineering, University of the Philippines, Diliman for the AY 2019-2020.

Author: Anica Galano - 2016-01120 
File Created: 1/30/2020
Development Group: CS 192 Group 5 
Client Group: CS 192 Group 5
Purpose of the Software: To provide mobile access of the DCS Codex with the feature of notifications for reminders. 

Code Histroy: 
1/30 - User model, Group model, Entry model 
1/31 - Added __str__ method for Group model
'''

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
     email = models.EmailField(unique=True) # Override Django user by making email unique
     
class Group(models.Model):
     name = models.CharField(max_length=50)
     users = models.ManyToManyField(User, related_name='groupz')
     def __str__(self):
     	return self.name # Provides string name of Group object

class Entry(models.Model):
     date = models.DateField()
     name = models.CharField(max_length=50)
     info = models.TextField(max_length=250)
     group = models.ForeignKey('Group', on_delete=models.CASCADE) # Each entry is related to a Group
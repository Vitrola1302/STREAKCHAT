from django.db import models

class MyProfile(models.Model):
    
    user = models.CharField(max_length=150)
    name = models.CharField(max_length=30)
    streak = models.IntegerField(default = 0)
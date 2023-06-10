from django.db import models

class MyProfile(models.Model):

    user = models.CharField(max_length=255, unique=True)
    name = models.TextField(max_length=30, default='')
    streak = models.IntegerField(default = 0)


    def getProfileByUsername(search):
        return MyProfile.objects.filter(user=search).get()
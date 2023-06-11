from typing import Any
from django.db import models

class MyProfile(models.Model):

    user = models.CharField(max_length=255, unique=True)
    name = models.TextField(max_length=30, default='')
    streak = models.IntegerField(default = 0)
    contact_list = models.OneToOneField('ContactList', on_delete=models.CASCADE, null=True, verbose_name="contact_list")

    def get_profile_by_username(search):
        return MyProfile.objects.filter(user=search).get()


class ContactList(models.Model):

    profile = models.OneToOneField('MyProfile', on_delete=models.CASCADE, null=True, verbose_name="profile")
    streak_value = models.IntegerField(default=0)
    
    def get_contact_by_username(self, search):
        return Contact.objects.filter(contact_list=self, user__user=search)


class Contact(models.Model):

    contact_list = models.ForeignKey('ContactList', on_delete=models.CASCADE, null=True, verbose_name="contact_list")
    user = models.ForeignKey(MyProfile, on_delete=models.CASCADE, verbose_name="user")
    name = models.TextField(max_length=30, default='New Contact') 
    streak = models.IntegerField(default=0)

    def get_streak(self):
        return self.streak
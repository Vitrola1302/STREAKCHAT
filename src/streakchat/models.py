from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    reciever = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    text = models.TextField(null=False, max_length=300)
    timestamp = models.DateTimeField(default=timezone.now)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    streak = models.IntegerField(default = 0)
    profile_picture = models.URLField(blank=True)

    def __str__(self):
        return f'Perfil de {self.user.username}'

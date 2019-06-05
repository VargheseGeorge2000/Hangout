from django.db import models
from django.contrib.auth.models import User


# Work on dm later with async
class Message(models.Model):
    message = models.CharField(max_length=200)
    author = models.CharField(max_length=30)
    datetime = models.DateTimeField()


class MyUser(models.Model):
    user = models.OneToOneField(User, related_name="useraccount", on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name="friends", blank=True)
    messages = models.ManyToManyField(Message, related_name="texts", blank=True)
    profile_picture = models.ImageField(default='default.png', blank=True)

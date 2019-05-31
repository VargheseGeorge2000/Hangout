from django.db import models


class Groups(models.Model):
    name = models.CharField(max_length=30)
    # Later on change to users maybe? But we'll stick with usernames as charfields
    # members = models.ManyToManyField(models.User)
    # manager = models.ForeignKey(models.User)
    manager = models.CharField(max_length=30)
    members = models.CharField(max_length=30)
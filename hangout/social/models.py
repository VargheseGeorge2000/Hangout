from django.db import models


class Events(models.Model):
    name = models.CharField(max_length=30)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_planned = models.DateField()
    location = models.CharField(max_length=100)
    cost_rating = models.CharField(max_length=100)


class Memories(models.Model):
    image = models.ImageField(blank=False)
    caption = models.CharField(max_length=100)
    date_posted = models.DateTimeField(auto_now_add=True)


class Groups(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(models.User)
    manager = models.ForeignKey(models.User)
    events = models.ManyToManyField(Events)
    memories = models.ManyToManyField(Memories)

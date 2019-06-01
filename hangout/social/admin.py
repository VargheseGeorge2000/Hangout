from django.contrib import admin
from . import models

admin.site.register(models.Memories)
admin.site.register(models.Events)
admin.site.register(models.Groups)
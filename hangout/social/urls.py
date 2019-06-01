from django.urls import path
from . import views
urlpatterns = [
    # GROUP
    path('group-create', views.group_create),
    # Edit and Delete in general need their ID as a parameter
    path('group-edit', views.group_edit),
    path('group-delete', views.group_delete),
    # EVENTS
    path('event-create', views.event_create),
    # Edit and Delete in general need their ID as a parameter
    path('event-edit', views.event_edit),
    path('event-delete', views.event_delete),
    # MEMORIES
    path('memory-add', views.memory_add),
    path('memory-delete', views.memory_delete),
]

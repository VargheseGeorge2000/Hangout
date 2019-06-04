from django.urls import path
from . import views
urlpatterns = [
    # LIST
    path('', views.social_home,name="home"),
    # GROUP
    path('group-create/', views.group_create, name="gcreate"),
    # Edit, View and Delete in general need their ID as a parameter
    path('group-view/<int:group_id>/', views.group_view, name="gview"),
    path('group-edit/<int:group_id>/', views.group_edit, name="gedit"),
    path('group-delete/<int:group_id>/', views.group_delete, name="gdelete"),
    # EVENTS
    path('event-create/<int:group_id>/', views.event_create, name="ecreate"),
    # Edit and Delete in general need their ID as a parameter
    path('event-edit/<int:event_id>/', views.event_edit, name="eedit"),
    path('event-delete/<int:event_id>/', views.event_delete, name="edelete"),
    # MEMORIES
    path('memory-add/<int:group_id>/', views.memory_add, name="madd"),
    path('memory-delete/<int:memory_id>/', views.memory_delete, name="mdelete"),
]

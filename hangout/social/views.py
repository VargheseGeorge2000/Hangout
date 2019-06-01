from django.shortcuts import render
from django.http import HttpResponse


def group_create(request):
    return HttpResponse("Create Group")


def group_edit(request):
    return HttpResponse("Edit Group")


def group_delete(request):
    return HttpResponse("Delete Group")


def event_create(request):
    return HttpResponse("Create Event")


def event_edit(request):
    return HttpResponse("Edit Event")


def event_delete(request):
    return HttpResponse("Delete Event")


def memory_add(request):
    return HttpResponse("Add Memory")


def memory_delete(request):
    return HttpResponse("Delete Memory")

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms


def social_home(request):
    return HttpResponse("Social Home")


# GROUPS
def group_create(request):
    print("GROUP-CREATE")
    if request.method == 'POST':
        group_form = forms.GroupForm(request.POST)
        print("Method is POST")
        if group_form.is_valid():
            print("New Group being Added")
            group_model = models.Groups(name=group_form.cleaned_data['name'], manager=request.user)
            group_model.save()
            print("Group Model : " + group_model.__str__() + " " + str(group_model.manager))
            # Must save before adding many to many field
            group_model.members.add(request.user)
            return redirect(to='home')
    else:
        print("Method is not POST")
        group_form = forms.GroupForm()

    return render(request, "social/group_create.html", {'form': group_form})



def group_edit(request, group_id):
    return HttpResponse("Edit Group")


def group_delete(request, group_id):
    return HttpResponse("Delete Group")


# EVENTS
def event_create(request):
    return HttpResponse("Create Event")


def event_edit(request, event_id):
    return HttpResponse("Edit Event")


def event_delete(request, event_id):
    return HttpResponse("Delete Event")


# MEMORIES
def memory_add(request):
    return HttpResponse("Add Memory")


def memory_delete(request, memory_id):
    return HttpResponse("Delete Memory")

from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models, forms
from django.contrib.auth.models import User
# All these methods should have a log in decorator that will redirect to the log in page
# Consider making the forms all a template to stylize


def social_home(request):
    groups = models.Groups.objects.filter(members=request.user)
    return render(request, "social/home.html", {'groups': groups})


def group_view(request, group_id):
    groups = models.Groups.objects.filter(members=request.user)
    group_model = models.Groups.objects.get(pk=group_id)
    if request.user == group_model.manager:
        is_manager = True
    else:
        is_manager = False
    members_list = group_model.members.all()
    # Test to see which needs to be reversed (might need to switch)
    # Want the closest upcoming events to show first
    memory_model = group_model.memories.all().order_by('date_posted').reverse()
    # Want the latest memories to show first
    event_model = group_model.events.all().order_by('datetime_planned')
    print(str(members_list))
    return render(request, "social/group_view.html", {'group_ref':group_model, 'events': event_model, 'memories': memory_model, "is_manager": is_manager, "members": members_list, "groups": groups})


# GROUPS
def group_create(request):
    print("GROUP-CREATE")
    if request.method == 'POST':
        group_form = forms.GroupForm(request.POST)
        print("Method is POST")
        if group_form.is_valid():
            print("New Group being Added")
            # JSON return from a form .cleaned_data
            group_model = models.Groups(name=group_form.cleaned_data['name'], manager=request.user)
            group_model.save()
            # All the print statements are for debugging purposes
            print("Group Model : " + group_model.__str__() + str(group_model.id))
            # Must save before adding many to many field
            group_model.members.add(request.user)
            return redirect(to='home')
    else:
        print("Method is not POST")
        group_form = forms.GroupForm()

    return render(request, "social/group_create.html", {'form': group_form})


# Will have modifications to members name and delete option
def group_edit(request, group_id):
    group_model = models.Groups.objects.get(pk=group_id)
    print("GROUP-EDIT")
    if request.method == 'POST':
        group_form = forms.GroupEditForm(request.POST)
        print("Method is POST")
        if group_form.is_valid():
            print("Valid Edit Form")
            # See if its to add or remove a member
            if request.POST['action'] == 'add':
                for member in group_form.cleaned_data["members"]:
                    group_model.members.add(member)
            # Otherwise it's delete
            else:
                for member in group_form.cleaned_data["members"]:
                    group_model.members.remove(member)
            group_model.name = group_form.cleaned_data["name"]
            group_model.save()
            print("Group Model : " + group_model.__str__())
            return redirect(to='home')
    else:
        print("Method is not POST")
        group_form = forms.GroupEditForm(instance=group_model)
    # Use this to auto fill the edit page
    return render(request, "social/group_edit.html", {'form': group_form, 'model': group_model})


def group_delete(request, group_id):
    print("GROUP-DELETE")
    group_model = models.Groups.objects.get(pk=group_id)
    print("Deleting: " + group_model.name)
    group_model.delete()
    return redirect(to='home')


# EVENTS
def event_create(request, group_id):
    print("EVENT-CREATE")
    group_model = models.Groups.objects.get(pk=group_id)
    if request.method == 'POST':
        event_form = forms.EventForm(request.POST)
        print("Method is POST")
        if event_form.is_valid():
            print("New Event being Added")
            # JSON return from a form .cleaned_data
            event_cleandata = event_form.cleaned_data
            event_model = models.Events(name=event_cleandata["name"], datetime_planned=event_cleandata["datetime_planned"], location=event_cleandata["location"], cost_rating=event_cleandata["cost_rating"])
            event_model.save()
            group_model.events.add(event_model)
            # All the print statements are for debugging purposes
            print("Event Model : " + event_model.__str__())
            # Must save before adding many to many field
            return redirect(to='gview', group_id=group_id)
    else:
        print("Method is not POST")
        event_form = forms.EventForm()

    return render(request, "social/event_create.html", {'form': event_form, "group": group_model})


def event_edit(request, group_id, event_id):
    print("EVENT-EDIT")
    event_model = models.Events.objects.get(pk=event_id)
    group_model = models.Groups.objects.get(pk=group_id)
    if request.method == 'POST':
        event_form = forms.EventForm(request.POST)
        print("Method is POST")
        if event_form.is_valid():
            print("Valid Edit Form")
            event_cleandata = event_form.cleaned_data
            event_model.name = event_cleandata["name"]
            event_model.datetime_planned = event_cleandata["datetime_planned"]
            event_model.location = event_cleandata["location"]
            event_model.cost_rating = event_cleandata["cost_rating"]
            event_model.save()
            # Edit the values of event to this
            print("Event Model : " + event_model.__str__())
            return redirect(to='gview', group_id=group_id)
    else:
        print("Method is not POST")
        event_form = forms.EventForm(instance=event_model)
    # Use this to auto fill the edit page
    return render(request, "social/event_edit.html", {'form': event_form, 'model': event_model,'group':group_model})


def event_delete(request, group_id, event_id):
    print("EVENT-DELETE")
    event_model = models.Events.objects.get(pk=event_id)
    event_model.delete()
    return redirect(to='gview', group_id=group_id)


# MEMORIES
def memory_add(request, group_id):
    print("MEMORY-CREATE")
    group_model = models.Groups.objects.get(pk=group_id)
    if request.method == 'POST':
        memory_form = forms.MemoryForm(request.POST, request.FILES)
        print("Method is POST")
        if memory_form.is_valid():
            print("New Memory being Added")
            memory_instance = memory_form.save()
            # All the print statements are for debugging purposes
            print("Memory Model : " + memory_instance.__str__())
            # Must save before adding many to many field (This part is faulty)
            group_model.memories.add(memory_instance)
            return redirect(to='gview', group_id=group_id)
        print("FORM IS NOT VALID")
    else:
        print("Method is not POST")
        memory_form = forms.MemoryForm()

    return render(request, "social/memory_add.html", {'form': memory_form, "group": group_model})


def memory_delete(request, group_id, memory_id):
    print("MEMORY-DELETE")
    memory_model = models.Memories.objects.get(pk=memory_id)
    memory_model.delete()
    # Logically, this makes sense to return to group view, maybe pass it as a parameter?
    return redirect(to='gview', group_id=group_id)

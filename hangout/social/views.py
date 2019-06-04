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
    group_model = models.Groups.objects.get(pk=group_id)
    if request.user == group_model.manager:
        is_manager = True
    else:
        is_manager = False
    members_list = group_model.members.all()
    # Test to see which needs to be reversed (might need to switch)
    # Want the closest upcoming events to show first
    memory_model = group_model.memories.all().order_by('date_posted')
    # Want the latest memories to show first
    event_model = group_model.events.all().order_by('datetime_planned').reverse()
    print(str(members_list))
    return render(request, "social/group_view.html", {'group': group_model, 'events': event_model, 'memories': memory_model, "is_manager": is_manager, "members": members_list})


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
            print("Group Model : " + group_model.str())
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
                group_model.members.add(group_form.cleaned_data["members"])
            # Otherwise it's delete
            else:
                group_model.members.remove(group_form.cleaned_data["members"])
            group_model.name = group_form.cleaned_data["name"]
            group_model.save()
            print("Group Model : " + group_model.str())
            return redirect(to='home')
    else:
        print("Method is not POST")
        group_form = forms.GroupEditForm(instance=group_model)
    # Use this to auto fill the edit page
    return render(request, "social/group_edit.html", {'form': group_form, 'model': group_model})


def group_delete(request, group_id):
    print("GROUP-DELETE")
    group_model = models.Groups.objects.get(pk=group_id)
    group_model.delete()
    return redirect(to='home')


# EVENTS
def event_create(request):
    print("EVENT-CREATE")
    return HttpResponse("Create Event")


def event_edit(request, event_id):
    return HttpResponse("Edit Event")


def event_delete(request, event_id):
    print("EVENT-DELETE")
    event_model = models.Events.objects.get(pk=event_id)
    event_model.delete()
    return redirect(to='home')


# MEMORIES
def memory_add(request, group_id):
    print("MEMORY-CREATE")
    group_model = models.Groups.objects.get(pk=group_id)
    if request.method == 'POST':
        memory_form = forms.MemoryForm(request.POST)
        print("Method is POST")
        if memory_form.is_valid():
            print("New Memory being Added")
            # JSON return from a form .cleaned_data
            memory_model = models.Memories(memory_form)
            memory_model.save()
            group_model.memories.add(memory_model)
            # All the print statements are for debugging purposes
            print("Memory Model : " + memory_model.__str__())
            # Must save before adding many to many field
            return redirect(to='home')
    else:
        print("Method is not POST")
        memory_form = forms.MemoryForm()

    return render(request, "social/memory_add.html", {'form': memory_form})


def memory_delete(request, memory_id):
    print("MEMORY-DELETE")
    memory_model = models.Memories.objects.get(pk=memory_id)
    memory_model.delete()
    # Logically, this makes sense to return to group view, maybe pass it as a parameter?
    return redirect(to='home')

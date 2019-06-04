from django import forms
from . import models

# If using a form for a specific model, reference forms.ModelForm in the parameter
# Then use Class Meta:


class GroupForm(forms.Form):
    name = forms.CharField(label="Group Name", max_length=100)


class GroupEditForm(forms.ModelForm):
    class Meta:
        model = models.Groups
        fields = ['name', 'members']


class EventForm(forms.ModelForm):
    class Meta:
        model = models.Events
        fields = ['name', 'datetime_planned', 'location', 'cost_rating']


class MemoryForm(forms.ModelForm):
    class Meta:
        model = models.Memories
        fields = ['image', 'caption']

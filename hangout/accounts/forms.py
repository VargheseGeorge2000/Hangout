from django import forms
from . import models

# If using a form for a specific model, reference forms.ModelForm in the parameter
# Then use Class Meta:


class SignUpForm(forms.Form):
    first_name = forms.CharField(label="First Name", max_length=100)
    last_name = forms.CharField(label="Last Name", max_length=100)
    profile_pic = forms.CharField(label="Profile Pic")

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import forms, models
from django.contrib.auth import login, logout, authenticate
# Create your views here.
# Added view to avoid mixing up login and login_view


def signup_view(request):
    if request.method == 'POST':
        # Creating a user account
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Log user in
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Name of app, then name of url to redirect
            # For some reason the redirect below failed (Out dated way?), so I'm hard coding it
            # return redirect('articles:list')
            return redirect('signup2')
    else:
        # Make a blank form and let them make their account
        form = UserCreationForm()
    # Outside of the else statement to consider case where form is not valid and fails saving, go back here
    return render(request, 'accounts/signup.html', {'form': form})


def signup2_view(request):
    user = request.user
    if request.method == 'POST':
        # Creating a user account
        form = forms.SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Log user in
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user_instance = models.MyUser(user=user, profile_pic=request.FILES['profile_pic'])
            user_instance.save()
            return redirect('home')
    else:
        # Make a blank form and let them make their account
        form = forms.SignUpForm()
    # Outside of the else statement to consider case where form is not valid and fails saving, go back here
    return render(request, 'accounts/signup.html', {'form': form})


# Validating log in
def login_view(request):
    if request.method == 'POST':
        # Needs to specify data since not normally first parameter
        form = AuthenticationForm(data=request.POST)
        # If valid form (log in fits?)
        if form.is_valid():
            # Log user in
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

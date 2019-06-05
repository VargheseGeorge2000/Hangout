from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
            return redirect('home')
    else:
        # Make a blank form and let them make their account
        form = UserCreationForm()
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

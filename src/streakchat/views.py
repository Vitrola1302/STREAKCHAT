from django.shortcuts import render
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, 'Registration Successful.')
            return render(request, 'landingpage/index.html')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

def loginPage(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'You are now logged in as {username}')  
                return render(request, 'home/index.html')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', context={'form':form})

def logoutPage(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return render(request, 'accounts/logout.html')

def landingPage(request):
    return render(request, 'landingpage/index.html')

def homePage(request):
    profile = profile = Profile.objects.get(user=request.user)
    streak = profile.streak
    return render(request, 'home/index.html', context={'streak':streak})
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import MyProfile

def homePage(request):
    logged_user = MyProfile.objects.get(user=request.user.id)
    streak = logged_user.streak
    return render(request, 'home/index.html', context={'streak':streak})


def registerPage(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            MyProfile.objects.create(user=request.user.id)
            messages.success(request, 'Registration Successful.')
            return homePage(request)
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
                return homePage(request)
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, "Invalid username or password")
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', context={'form':form})


def logoutRequest(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return landingPage(request)


def landingPage(request):
    return render(request, 'landingpage/index.html')
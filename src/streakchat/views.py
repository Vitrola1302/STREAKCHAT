from django.shortcuts import render, redirect
from .forms import RegisterForm, NameForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import MyProfile


def registerPage(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            registered_user = form.save()
            login(request, registered_user)
            MyProfile.objects.create(user=registered_user.username)
            messages.success(request, 'Registration Successful.')
            return homePage(request)
        
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')

    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


def loginPage(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

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



def firstLoginPage(request):

    logged_user = MyProfile.getProfileByUsername(request.user.username)

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            logged_user.name = form.cleaned_data["name"]
            logged_user.save()
            return homePage(request)

    else:
        form = NameForm()

    return render(request, 'accounts/firstlogin.html', context={'form':form})


def landingPage(request):
    return render(request, 'landingpage/index.html')


def homePage(request):

    logged_user = MyProfile.getProfileByUsername(request.user.username)

    if logged_user.name == '':    
        return firstLoginPage(request)
    
    name = logged_user.name
    streak = logged_user.streak
    return render(request, 'home/index.html', context={'name':name,'streak':streak})


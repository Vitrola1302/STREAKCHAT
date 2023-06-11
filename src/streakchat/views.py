from django.shortcuts import render, redirect
from .forms import RegisterForm, NameForm, AddContactForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import MyProfile, ContactList, Contact


def registerPage(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            registered_user = form.save()
            login(request, registered_user)
            new_profile = MyProfile.objects.create(user=registered_user.username)
            messages.success(request, 'Registration Successful.')
            return redirect('/home')
        
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
                return redirect('/home')
            
            else:
                messages.error(request, 'Invalid username or password.')

        else:
            messages.error(request, "Invalid username or password")

    form = AuthenticationForm()
    return render(request, 'accounts/login.html', context={'form':form})


def logoutRequest(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
         
	return redirect('/')



def firstLoginPage(request):

    logged_user = MyProfile.get_profile_by_username(request.user.username)

    if request.method == 'POST':
        form = NameForm(request.POST)

        if form.is_valid():
            logged_user.name = form.cleaned_data["name"]
            logged_user.save()
            return redirect('/home')

    else:
        form = NameForm()

    return render(request, 'accounts/firstlogin.html', context={'form':form})


def landingPage(request):
    return render(request, 'landingpage/index.html')


def homePage(request):

    logged_user = MyProfile.get_profile_by_username(request.user.username)

    if logged_user.name == '':    
        return firstLoginPage(request)
    
    contacts = list(Contact.objects.filter(contact_list=logged_user.contact_list))
    contacts.sort(key=Contact.get_streak)

    return render(request, 'home/index.html', context={'user':logged_user, 'contacts':contacts})


def addContactPage(request):
    
    logged_user = MyProfile.get_profile_by_username(request.user.username)

    if request.method == 'POST':
        form = AddContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            username = form.cleaned_data["username"]

            #se o usuário descrito não existe
            if not MyProfile.objects.filter(user=username).exists():
                messages.error(request, 'Threre is no user with the informed username.')

            else:
                #lista de contatos do usuário vazia, cria uma nova
                if not logged_user.contact_list:
                    new_contact_list = ContactList.objects.create(profile=logged_user)
                    logged_user.contact_list = new_contact_list
                    logged_user.save()

                #se o contato já existe na lista de contatos do usuário
                if logged_user.contact_list.get_contact_by_username(username).exists():
                    messages.error(request, f'You already have {name} in your contact list.')
                
                #adiciona o contato na lista
                else:
                    new_contact = MyProfile.objects.filter(user=username).get()
                    Contact.objects.create(contact_list=logged_user.contact_list, user=new_contact, name=name)
                    messages.info(request, f'{name} successfully added to {logged_user.name}\'s contact list.')
                    
    else:
        form = AddContactForm()

    return render(request, 'home/addcontact.html', context={'form':form})
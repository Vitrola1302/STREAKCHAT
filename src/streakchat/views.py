from django.shortcuts import render, redirect
from .forms import RegisterForm

def registerPage(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    return render(request, 'accounts/register.html', {'form':form})

def loginPage(request):
    return render(request, 'accounts/login.html')

def landingPage(request):
    return render(request, 'landingpage/index.html')


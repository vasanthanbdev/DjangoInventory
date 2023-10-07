from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# register page
def register_user(request):
    if request.method == "POST":
        form = UserRegistery(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = UserRegistery()
        context = {"form":form}
        return render(request, "register_user.html", context)
    
    
#login page
def login_user(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        forms = LoginForm()
        context = {'form': forms}
        return render(request, 'login_user.html', context)


#logout user
@login_required
def logout_user(request):
    logout(request)
    return redirect(request, "home.html")
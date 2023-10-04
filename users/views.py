from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def register_user(request):
    if request.method == "POST":
        form = UserRegistery(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(request, "home.html")
    else:
        form = UserRegistery()
        context = {"form":form}
        return render(request, "register_user.html", context)

@login_required
def logout_user(request):
    logout(request)
    return redirect(request, "home.html")
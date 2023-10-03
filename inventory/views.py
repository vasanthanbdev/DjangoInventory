from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import *
from .models import *

# Create your views here.
def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request, "home.html")
        return redirect(request, "home.html")
    else:
        return render(request, "home.html")
    
def register_user(request):
    if request.method == "POST":
        form = UserRegistery(request.POST)
        if form.is_valid:
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(request, "home.html")
    else:
        form = UserRegistery()
        return render(request, "register_user.html", {"form":form})

def logout_user(request):
    logout(request)
    return redirect(request, "home.html")

def products(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        return render(request, "products.html", {"products":products})

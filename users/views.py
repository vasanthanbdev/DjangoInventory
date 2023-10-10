from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views import View
from .forms import *
from .models import *

# register page
class RegisterUserView(View):
    def get(self, request):
        form = UserRegistration()
        context = {"form": form}
        return render(request, "register_user.html", context)

    def post(self, request):
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
        context = {"form": form}
        return render(request, "register_user.html", context)
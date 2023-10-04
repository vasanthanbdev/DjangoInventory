from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
@login_required
def products(request):
    products = Product.objects.all()
    if request.user.is_authenticated:
        return render(request, "products.html", {"products":products})

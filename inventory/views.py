from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import *
from .models import *

# Product views
@login_required
def products(request):
    products = Product.objects.all()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    else:
        form = ProductForm()
    context = {
        "title": "Products",
        "products": products,
        "form": form
    }
    return render(request, 'products.html', context)
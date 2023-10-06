from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "quantity", "reorder_level"]
        
# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ["product"]

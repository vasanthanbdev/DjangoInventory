from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegistery(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "firstname", "lastname", "password1", "password2"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "quantity"]
        
# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ["product"]

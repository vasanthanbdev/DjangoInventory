from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "quantity", "purchase_price", "sale_price"]
        
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["product"]
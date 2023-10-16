from rest_framework import serializers
from .models import *

#products
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'quantity', 'preferred_vendor', 'reorder_level']
        
#warehouses
class WarehouseSeializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['name', 'email', 'contact', 'city', 'address']


#vendors
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'email', 'contact', 'city', 'address']
        

# #customers
# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = ['name', 'email', 'contact', 'city', 'address']
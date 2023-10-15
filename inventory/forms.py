from django import forms
from .models import *

#products
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'category', 'price', 'quantity', 'preferred_vendor', 'reorder_level']
        
# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ['product']


#warehouses
class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'email', 'contact', 'city', 'address']


#vendors
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'email', 'contact', 'city', 'address']
        

#customers
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'contact', 'city', 'address']

#purchase_orders
# class PurchaseOrderForm(forms.ModelForm):
#     class Meta:
#         model = PurchaseOrder
#         fields = ['order_date', 'delivery_date', 'vendor', 'warehouse', 'products']

# #sales orders
# class SalesOrderForm(forms.ModelForm):
#     class Meta:
#         model = SalesOrder
#         fields = ['order_date', 'delivery_date', 'customer', 'products', 'status']

# #invoices
# class InvoiceForm(forms.ModelForm):
#     class Meta:
#         model = Invoice
#         fields = ['customer', 'sales_order', 'invoice_date', 'due_date', 'products']
        
# #bills
# class BillForm(forms.ModelForm):
#     class Meta:
#         model = Bill
#         fields = ['vendor', 'purchase_order', 'bill_date', 'due_date', 'products']
        
# #packages
# class PackageForm(forms.ModelForm):
#     class Meta:
#         model = Package
#         fields = []

# #carrier
# class CarrierForm(forms.ModelForm):
#     class Meta:
#         model = Carrier
#         fields = ["name"]
from django import forms
from .models import *

#products
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "category", "price", "quantity", "reorder_level"]
        
# class ItemForm(forms.ModelForm):
#     class Meta:
#         model = Item
#         fields = ["product"]


#warehouses
class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ["name", "city", "address", "contact"]


#vendors
class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ["name", "email", "contact", "city", "address"]
        

#customers
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "email", "contact", "city", "address"]

#purchase_orders
class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = []

#sales orders
class SalesOrderForm(forms.ModelForm):
    class Meta:
        model = SalesOrder
        fields = []

#invoices
class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = []
        
#bills
class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = []
        
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
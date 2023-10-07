from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .forms import *
from .models import *


# Product views
@login_required
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

@login_required
def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')  
    else:
        form = ProductForm()
    
    context = {'form': form}
    return render(request, 'create_product.html', context)


# warehouse
@login_required
class WarehouseListView(ListView):
    model = Warehouse
    template_name = 'warehouse_list.html'
    context_object_name = 'warehouses'

@login_required
def create_warehouse(request):
    if request.method == 'POST':
        form = WarehouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('warehouse_list')  
    else:
        form = WarehouseForm()
    
    context = {'form': form}
    return render(request, 'create_warehouse.html', context)


#vendors
@login_required
class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor_list.html'
    context_object_name = 'vendors'

@login_required
def create_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')  
    else:
        form = VendorForm()
    
    context = {'form': form}
    return render(request, 'create_vendor.html', context)


#customer
@login_required
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customer'
    
@login_required
def create_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')  
    else:
        form = CustomerForm()
    
    context = {'form': form}
    return render(request, 'create_customer.html', context)


#purchase orders
@login_required
class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = 'purchase_order_list.html'
    context_object_name = 'purchase_order'

@login_required
def create_purchase_order(request):
    if request.method == 'POST':
        form = PurchaseOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('purchase_order_list')  
    else:
        form = PurchaseOrderForm()
    
    context = {'form': form}
    return render(request, 'create_purchase_order.html', context)


#sales order
@login_required
class SalesOrderListView(ListView):
    model = SalesOrder
    template_name = 'sales_order_list.html'
    context_object_name = 'sales_order'

@login_required
def create_sales_order(request):
    if request.method == 'POST':
        form = SalesOrder(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sales_order_list')  
    else:
        form = SalesOrderForm()
    
    context = {'form': form}
    return render(request, 'create_sales_order.html', context)


#Bill
@login_required
class BillListView(ListView):
    model = Bill
    template_name = 'bill_list.html'
    context_object_name = 'bill'

@login_required
def create_bill(request):
    if request.method == 'POST':
        form = BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill_list')  
    else:
        form = BillForm()
    
    context = {'form': form}
    return render(request, 'create_bill.html', context)


#invoice
@login_required
class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice_list.html'
    context_object_name = 'invoice'

@login_required
def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')  
    else:
        form = InvoiceForm()
    
    context = {'form': form}
    return render(request, 'create_invoice.html', context)


#package
@login_required
class PackageListView(ListView):
    model = Package
    template_name = 'package_list.html'
    context_object_name = 'package'

@login_required
def create_package(request):
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('package_list')  
    else:
        form = PackageForm()
    
    context = {'form': form}
    return render(request, 'create_package.html', context)


#carrier
@login_required
class CarrierListView(ListView):
    model = Carrier
    template_name = 'carrier_list.html'
    context_object_name = 'carrier'

@login_required
def create_carrier(request):
    if request.method == 'POST':
        form = CarrierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carrier_list')  
    else:
        form = CarrierForm()
    
    context = {'form': form}
    return render(request, 'create_carrier.html', context)
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import *
from .models import *


# Product views
@method_decorator(login_required, name='dispatch')
class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    
@method_decorator(login_required, name='dispatch')
class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'create_product.html'
    success_url = reverse_lazy('product_list')
    
    def form_valid(self, form):
        return super().form_valid(form)


# warehouse
@method_decorator(login_required, name='dispatch')
class WarehouseListView(ListView):
    model = Warehouse
    template_name = 'warehouse_list.html'
    context_object_name = 'warehouses'

@method_decorator(login_required, name='dispatch')
class WarehouseCreateView(CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'create_warehouse.html'
    success_url = reverse_lazy('warehouse_list')

    def form_valid(self, form):
        return super().form_valid(form)
    

#vendors
@method_decorator(login_required, name='dispatch')
class VendorListView(ListView):
    model = Vendor
    template_name = 'vendor_list.html'
    context_object_name = 'vendors'

@method_decorator(login_required, name='dispatch')
class VendorCreateView(CreateView):
    model = Vendor
    form_class = VendorForm
    template_name = 'create_vendor.html'
    success_url = reverse_lazy('vendor_list')

    def form_valid(self, form):
        return super().form_valid(form)


#customer
@method_decorator(login_required, name='dispatch')
class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customer'
    
@method_decorator(login_required, name='dispatch')
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'create_customer.html'
    success_url = reverse_lazy('customer_list')

    def form_valid(self, form):
        return super().form_valid(form)


#purchase orders
@method_decorator(login_required, name='dispatch')
class PurchaseOrderListView(ListView):
    model = PurchaseOrder
    template_name = 'purchase_order_list.html'
    context_object_name = 'purchase_order'

@method_decorator(login_required, name='dispatch')
class PurchaseOrderCreateView(CreateView):
    model = PurchaseOrder
    form_class = PurchaseOrderForm
    template_name = 'create_purchase_order.html'
    success_url = reverse_lazy('purchase_order_list')

    def form_valid(self, form):
        return super().form_valid(form)


#sales order
@method_decorator(login_required, name='dispatch')
class SalesOrderListView(ListView):
    model = SalesOrder
    template_name = 'sales_order_list.html'
    context_object_name = 'sales_order'

@method_decorator(login_required, name='dispatch')
class SalesOrderCreateView(CreateView):
    model = SalesOrder
    form_class = SalesOrderForm
    template_name = 'create_sales_order.html'
    success_url = reverse_lazy('sales_order_list')

    def form_valid(self, form):
        return super().form_valid(form)
    
    
#Bill
@method_decorator(login_required, name='dispatch')
class BillListView(ListView):
    model = Bill
    template_name = 'bill_list.html'
    context_object_name = 'bill'

@method_decorator(login_required, name='dispatch')
class BillCreateView(CreateView):
    model = Bill
    form_class = BillForm
    template_name = 'create_bill.html'
    success_url = reverse_lazy('bill_list')

    def form_valid(self, form):
        return super().form_valid(form)


#invoice
@method_decorator(login_required, name='dispatch')
class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoice_list.html'
    context_object_name = 'invoice'

@method_decorator(login_required, name='dispatch')
class InvoiceCreateView(CreateView):
    model = Invoice
    form_class = InvoiceForm
    template_name = 'create_invoice.html'
    success_url = reverse_lazy('invoice_list')

    def form_valid(self, form):
        return super().form_valid(form)


# #package
# @method_decorator(login_required, name='dispatch')
# class PackageListView(ListView):
#     model = Package
#     template_name = 'package_list.html'
#     context_object_name = 'package'

# @method_decorator(login_required, name='dispatch')
# class PackageCreateView(CreateView):
#     model = Package
#     form_class = PackageForm
#     template_name = 'create_package.html'
#     success_url = reverse_lazy('package_list')

#     def form_valid(self, form):
#         return super().form_valid(form)


# #carrier
# @method_decorator(login_required, name='dispatch')
# class CarrierListView(ListView):
#     model = Carrier
#     template_name = 'carrier_list.html'
#     context_object_name = 'carrier'

# @method_decorator(login_required, name='dispatch')
# class CarrierCreateView(CreateView):
#     model = Carrier
#     form_class = CarrierForm
#     template_name = 'create_carrier.html'
#     success_url = reverse_lazy('carrier_list')

#     def form_valid(self, form):
#         return super().form_valid(form)
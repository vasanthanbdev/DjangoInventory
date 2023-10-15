from django.urls import path
from .views import *


urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='create_product'),

    path('warehouses/', WarehouseListView.as_view(), name='warehouse_list'),
    path('warehouses/create/', WarehouseCreateView.as_view(), name='create_warehouse'),

    path('vendors/', VendorListView.as_view(), name='vendor_list'),
    path('vendors/create/', VendorCreateView.as_view(), name='create_vendor'),

    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', CustomerCreateView.as_view(), name='create_customer'),
    
    # path('purchase_orders/', PurchaseOrderListView.as_view(), name='purchase_order_list'),
    # path('purchase_orders/create/', PurchaseOrderCreateView.as_view(), name='create_purchase_order'),

    # path('sales_orders/', SalesOrderListView.as_view(), name='sales_order_list'),
    # path('sales_order/create/', SalesOrderCreateView.as_view(), name='create_sales_order'),

    # path('invoices/', InvoiceListView.as_view(), name='invoice_list'),
    # path('invoices/create/', InvoiceCreateView.as_view(), name='create_invoice'),
    
    # path('bills/', BillListView.as_view(), name='bill_list'),
    #  path('bills/create/', BillCreateView.as_view(), name='create_bill'),

    # path('packages/', PackageListView.as_view(), name='package_list'),
    # path('packages/create/', PackageCreateView.as_view(), name='create_package'),
    
    # path('carriers/', CarrierListView.as_view(), name='carrier_list'),
    # path('carriers/create/', CarrierCreateView.as_view(), name='create_carrier'),
]


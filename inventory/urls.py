from django.urls import path, include
from .views import (
    ProductListView,
    create_product,
    WarehouseListView,
    create_warehouse,
    VendorListView,
    create_vendor,
    CustomerListView,
    create_customer,
    PurchaseOrderListView,
    create_purchase_order,
    SalesOrderListView,
    create_sales_order,
    InvoiceListView,
    create_invoice,
    BillListView,
    create_bill,
    PackageListView,
    create_package,
    CarrierListView,
    create_carrier,
)



urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', create_product, name='create_product'),

    path('warehouse/', WarehouseListView.as_view(), name='warehouse_list'),
    path('warehouse/create/', create_warehouse, name='create_warehouse'),

    path('vendors/', VendorListView.as_view(), name='vendor_list'),
    path('vendors/create/', create_vendor, name='create_vendor'),

    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/create/', create_customer, name='create_customer'),

    path('purchase_orders/', PurchaseOrderListView.as_view(), name='purchase_order_list'),
    path('purchase_orders/create/', create_purchase_order, name='create_purchase_order'),

    path('sales_orders/', SalesOrderListView.as_view(), name='sales_order_list'),
    path('sales_orders/create/', create_sales_order, name='create_sales_order'),

    path('invoices/', InvoiceListView.as_view(), name='invoice_list'),
    path('invoices/create/', create_invoice, name='create_invoice'),

    path('bills/', BillListView.as_view(), name='bill_list'),
    path('bills/create/', create_bill, name='create_bill'),

    path('packages/', PackageListView.as_view(), name='package_list'),
    path('packages/create/', create_package, name='create_package'),

    path('carriers/', CarrierListView.as_view(), name='carrier_list'),
    path('carriers/create/', create_carrier, name='create_carrier'),
]


# app_name = 'inventory'  

# # Include the app's URL patterns
# urlpatterns = [
#     path('inventory/', include((urlpatterns, app_name), namespace=app_name)),
# ]

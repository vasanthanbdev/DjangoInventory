from django.contrib import admin
from .models import *

admin.site.register(Vendor)
admin.site.register(Product)
# admin.site.register(Item)
admin.site.register(Warehouse)
admin.site.register(Customer)

# admin.site.register(PurchaseOrder)
# admin.site.register(PurchaseOrderItem)
# admin.site.register(SalesOrder)
# admin.site.register(SalesOrderItem)
# admin.site.register(Invoice)
# admin.site.register(InvoiceItem)
# admin.site.register(Bill)
# admin.site.register(BillItem)

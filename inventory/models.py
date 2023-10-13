from django.db import models
from uuid import uuid4
from .constants import *
from django.db.models import Sum, F
from django.utils import timezone


#Vendor model
class Vendor(models.Model):
    id = models.UUIDField(primary_key=True, default='VD-'+str(uuid4()).split('-')[1])
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)  
    contact = models.CharField(max_length=15, null=True)
    city = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


# Product and Item models
class Product(models.Model):
    id = models.UUIDField(primary_key=True, default='PR-'+str(uuid4()).split('-')[1])
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=1000, blank=True, default='')
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(null=True)
    preferred_vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT, null=True)
    reorder_level = models.PositiveIntegerField(default=2)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name
    
    
# class Item(models.Model):
#     id = models.UUIDField(primary_key=True, default='ITM-'+str(uuid4()).split('-')[1])
#     product = models.ForeignKey(Product, on_delete=models.PROTECT)
#     status = models.CharField(max_length=100, choices=ITEM_STATUS, null=True)
#     Vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
#     Warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
#     Customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
#     # Carrier = models.ForeignKey(Carrier, on_delete=models.PROTECT)
    
#     class Meta:
#         ordering = ['id']
    
#     def __str__(self) -> str:
#         return f"{self.product} - {self.id}"
    

#warehouse model 
class Warehouse(models.Model):
    id = models.UUIDField(primary_key=True, default='WH-'+str(uuid4()).split('-')[1])
    name = models.CharField(max_length=100, null=True)
    contact = models.EmailField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.TextField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"{self.name} - {self.id}"


#customer model
class Customer(models.Model):
    id = models.UUIDField(primary_key=True, default='CO-'+str(uuid4()).split('-')[1])
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100)  
    contact = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    address = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name} - {self.id}"


#Purchase order
class PurchaseOrder(models.Model):
    id = models.UUIDField(primary_key=True, default='PO-'+str(uuid4()).split('-')[1])
    order_date = models.DateField(default=timezone.now)
    delivery_date = models.DateField()
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, through='PurchaseOrderItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def save(self, *args, **kwargs):
        self.total_price = self.products.aggregate(
            total_price=Sum(F('purchaseorderitem__total_item_price'))
        )['total_price'] or 0.0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Purchase Order No: {self.id}"

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    quantity = models.PositiveIntegerField(default=1)
    total_item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        self.total_item_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
    

#Sales order
class SalesOrder(models.Model):
    id = models.UUIDField(primary_key=True, default='PO-'+str(uuid4()).split('-')[1])
    order_date = models.DateField(default=timezone.now)
    delivery_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, through='SalesOrderItem')
    status = models.CharField(max_length=100, choices=SALES_STATUS, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def save(self, *args, **kwargs):
        self.total_price = self.products.aggregate(
            total_price=Sum(F('salesorderitem__total_item_price'))
        )['total_price'] or 0.0
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Purchase Order No: {self.id}"

class SalesOrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    quantity = models.PositiveIntegerField(default=1)
    total_item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        self.total_item_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

    
    
#Bill
class Bill(models.Model):
    # invoice_number = models.CharField(max_length=50, unique=True, default='WH-'+str(uuid4()).split('-')[1])
    id = models.UUIDField(primary_key=True, default='BL-'+str(uuid4()).split('-')[1])
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.PROTECT)
    bill_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    products = models.ManyToManyField(Product, through='BillItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total_price = self.products.aggregate(
            total_price=Sum(F('billitem__total_item_price'))
        )['total_price'] or 0.0
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Bill No : {self.id}" 

class BillItem(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.PROTECT, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    quantity = models.PositiveIntegerField()
    total_item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        self.total_item_price = self.product.price * self.quantity
        super().save(*args, **kwargs)
    
      
#Invoice
class Invoice(models.Model):
    # invoice_number = models.CharField(max_length=50, unique=True, default='WH-'+str(uuid4()).split('-')[1])
    id = models.UUIDField(primary_key=True, default='INV-'+str(uuid4()).split('-')[1])
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.PROTECT)
    invoice_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    products = models.ManyToManyField(Product, through='InvoiceItem')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def save(self, *args, **kwargs):
        self.total_price = self.products.aggregate(
            total_price=Sum(F('invoiceitem__total_item_price'))
        )['total_price'] or 0.0
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Invoice No : {self.id}" 

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, null=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    quantity = models.PositiveIntegerField()
    total_item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def save(self, *args, **kwargs):
        self.total_item_price = self.product.price * self.quantity
        super().save(*args, **kwargs)

      
    
# #Carrier
# class Carrier(models.Model):
#     name = models.CharField(max_length=100, null=True)
    
#     def __str__(self) -> str:
#         return f"Name: {self.name}"
    

# #Package
# class Package(models.Model):
#     package_number = models.CharField(max_length=50, unique=True, default='WH-'+str(uuid4()).split('-')[1])
#     package_date = models.DateField(auto_now_add=True)
#     carrier = models.ForeignKey(Carrier, on_delete=models.PROTECT)
#     sales_order = models.ForeignKey(SalesOrder, on_delete=models.PROTECT)
#     status = models.CharField(max_length=100, choices=PACKAGE_STATUS, null=True)
#     shipment_date = models.DateField()
#     customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
#     quantity_ordered = models.PositiveIntegerField()
    
#     def __str__(self):
#         return f"Package Number: {self.package_number}"


  
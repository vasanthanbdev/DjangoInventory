from django.db import models
import uuid
from .constants import *


# Product and Item models
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100, choices=CATEGORY, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    quantity = models.PositiveIntegerField(null=True)
    reorder_level = models.PositiveIntegerField(default=10)
    
    def __str__(self) -> str:
        return self.name
    
class Item(models.Model):
    serial_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4().hex[:12].upper())
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return f"{self.product} - Serial Number: {self.serial_number}"
    

#warehouse model 
class Warehouse(models.Model):
    warehouse_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4().hex[:12].upper())
    name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    contact = models.EmailField()
    
    def __str__(self) -> str:
        return self.warehouse_number


#Vendor model
class Vendor(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)  # Use CharField with max_length for email
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

#customer model
class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)  # Use CharField with max_length for email
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


#Purchase order
class PurchaseOrder(models.Model):
    PurchaseOrdernumber = models.CharField(max_length=50, unique=True, default=uuid.uuid4().hex[:12].upper())
    Vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    order_date = models.DateField()
    delivery_date = models.DateField()
    items = models.ManyToManyField(Item, through='PurchaseOrderItem')
    item_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"OrderNo : {self.PurchaseOrdernumber}"

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Item: {self.item}, Quantity: {self.quantity_ordered}"
    

#Sales order
class SalesOrder(models.Model):
    SalesOrdernumber = models.CharField(max_length=50, unique=True, default=uuid.uuid4().hex[:12].upper())
    order_date = models.DateField()
    Customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    status = models.CharField(max_length=100, choices=SALES_STATUS, null=True)
    invoiced = models.BooleanField()
    packed = models.BooleanField()
    shipped = models.BooleanField()
    delivery_date = models.DateField()
    items = models.ManyToManyField(Item, through='SalesOrderItem')
    item_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    
    def __str__(self) -> str:
        return f"OrderNo : {self.SalesOrdernumber}"

class SalesOrderItem(models.Model):
    SalesOrder = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Item: {self.item}, Quantity: {self.quantity_ordered}"
    
    
#Bill
class Bill(models.Model):
    bill_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4().hex[:12].upper())
    Vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    PurchaseOrder = models.ForeignKey(PurchaseOrder, on_delete=models.PROTECT)
    Warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    bill_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True)
    items = models.ManyToManyField(Item, through='BillItem')
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f"Bill No : {self.bill_number}" 

class BillItem(models.Model):
    Bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item: {self.item}, Quantity: {self.quantity_ordered}"
    
      
#Invoice
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4().hex[:12].upper())
    Customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    SalesOrder = models.ForeignKey(SalesOrder, on_delete=models.PROTECT)
    invoice_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True)
    items = models.ManyToManyField(Item, through='InvoiceItem')
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self) -> str:
        return f"Invoice No : {self.invoice_number}" 

class InvoiceItem(models.Model):
    Invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Item: {self.item}, Quantity: {self.quantity_ordered}"
      
    
#Carrier
class Carrier(models.Model):
    name = models.CharField(max_length=100, null=True)
    
    def __str__(self) -> str:
        return f"Name: {self.name}"
    

#Package
class Package(models.Model):
    package_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4().hex[:12].upper())
    package_date = models.DateField(auto_now_add=True)
    carrier = models.ForeignKey(Carrier, on_delete=models.PROTECT)
    sales_order = models.ForeignKey(SalesOrder, on_delete=models.PROTECT)
    status = models.CharField(max_length=100, choices=PACKAGE_STATUS, null=True)
    shipment_date = models.DateField()
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    quantity_ordered = models.PositiveIntegerField()
    
    def __str__(self):
        return f"Package Number: {self.package_number}"


  
from django.db import models
import uuid
from .constants import *


# Product and Item models
class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(default=0.0)
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
    contact = models.EmailField()
    city = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    
    def __str__(self) -> str:
        return self.warehouse_number


#Vendor model
class Vendor(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)  # Use CharField with max_length for email
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    

#customer model
class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, unique=True)  # Use CharField with max_length for email
    contact = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


#Purchase order
class PurchaseOrder(models.Model):
    purchase_order_number = models.CharField(max_length=50, unique=True, default=uuid.uuid4().hex[:12].upper())
    order_date = models.DateField(auto_now_add=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.PROTECT)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.PROTECT)
    delivery_date = models.DateField()
    products = models.ManyToManyField(Product, through='PurchaseOrderProduct')
    total_no_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def total_no_products_count(self):
        return self.products.count()
    
    def total_price_calc(self):
        total_price = 0
        for purchase_order_product in self.products.all():
            total_price += purchase_order_product.total_item_price
        return total_price

    def save(self, *args, **kwargs):
        self.total_no_products = self.total_no_products_count()
        self.total_price = self.total_price_calc()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Purchase Order No: {self.purchase_order_number}"

class PurchaseOrderProduct(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    sno = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(max_length=10, default=1)
    total_item_price = models.DecimalField(max_digits=10, decimal_places=2)

    def total_item_price_clac(self):
        return self.unit_price * self.quantity

    def save(self, *args, **kwargs):
        self.total_item_price = self.total_item_price_clac()
        super().save(*args, **kwargs)
    

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
    item_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    
    def __str__(self) -> str:
        return f"OrderNo : {self.SalesOrdernumber}"

class SalesOrderItem(models.Model):
    SalesOrder = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

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


  
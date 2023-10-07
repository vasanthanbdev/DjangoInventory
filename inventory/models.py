from django.db import models
import uuid

CATEGORY = (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food')
)

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
    serial_number = models.CharField(max_length=50, unique=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not self.serial_number:
            # Generate a unique serial number (e.g., using UUID)
            self.serial_number = str(uuid.uuid4().hex[:12].upper())
        super(Item, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return f"{self.product} - Serial Number: {self.serial_number}"
    

#warehouse model 
class Warehouse(models.Model):
    Warehouse_id = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    contact = models.EmailField()
    
    def save(self, *args, **kwargs):
        if not self.serial_number:
            # Generate a unique serial number (e.g., using UUID)
            self.Warehouse_id = str(uuid.uuid4().hex[:12].upper())
        super(Item, self).save(*args, **kwargs)
    
    def __str__(self) -> str:
        return self.Warehouse_id


#Vendor model
class Vendor(models.Model):
    name = models.CharField(max_length=100, null=True)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name
    

#customer model
class Customer(models.Model):
    name = models.CharField(max_length=100, null=True)
    email =  models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address =  models.CharField(max_length=100)
    city =  models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name


#Purchase order
class PurchaseOrder(models.Model):
    PurchaseOrdernumber = models.CharField(max_length=50, unique=True)
    Vendor = models.ForeignKey(Vendor)
    Warehouse = models.ForeignKey(Warehouse)
    order_date = models.DateField()
    delivery_date = models.DateField()
    items = models.ManyToManyField(Item, through='PurchaseOrderItem')
    item_price = models.DecimalField(decimal_places=2)
    total_price = models.DecimalField(decimal_places=2)
    
    
    def save(self, *args, **kwargs):
        if not self.serial_number:
            # Generate a unique serial number (e.g., using UUID)
            self.PurchaseOrdernumber = str(uuid.uuid4().hex[:12].upper())
        super(Item, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f"Vendor: {self.Vendor}, OrderNo : {self.PurchaseOrdernumber}" 
        
      
class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"Item: {self.item}, Quantity: {self.quantity_ordered}"
    

STATUS = (
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Closed', 'Closed')
)


#Sales order
class SalesOrder(models.Model):
    SalesOrdernumber = models.CharField(max_length=50, unique=True)
    order_date = models.DateField()
    Customer = models.ForeignKey(Customer)
    status = models.CharField(max_length=100, choices=CATEGORY, null=True)
    invoiced = models.BooleanField()
    packed = models.BooleanField()
    shipped = models.BooleanField()
    delivery_date = models.DateField()
    items = models.ManyToManyField(Item, through='SalesOrderItem')
    item_price = models.DecimalField(decimal_places=2)
    total_price = models.DecimalField(decimal_places=2)
    
    
    def save(self, *args, **kwargs):
        if not self.serial_number:
            # Generate a unique serial number (e.g., using UUID)
            self.SalesOrdernumber = str(uuid.uuid4().hex[:12].upper())
        super(Item, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return f"Customer: {self.Customer}, OrderNo : {self.SalesOrdernumber}" 
        
      
class SalesOrderItem(models.Model):
    purchase_order = models.ForeignKey(SalesOrder, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_ordered = models.PositiveIntegerField()
    unit_price = models.DecimalField(decimal_places=2)

    def __str__(self):
        return f"Item: {self.item}, Quantity: {self.quantity_ordered}"
    
    
#Invoice
class Invoice(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    Vendor = models.ForeignKey(Vendor)
    PurchaseOrder = models.ForeignKey(PurchaseOrder)
    invoice_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=True)
    
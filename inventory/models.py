from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(null=True)
    
    def __str__(self) -> str:
        return self.name
    
# class Item(models.Model):
#     serial_number = models.CharField(max_length=50, unique=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

#     def save(self, *args, **kwargs):
#         if not self.serial_number:
#             # Generate a unique serial number (e.g., using UUID)
#             self.serial_number = str(uuid.uuid4())
#         super(Item, self).save(*args, **kwargs)
    
#     def __str__(self) -> str:
#         return f"{self.product} - Serial Number: {self.serial_number}"

# from django.db import models
# import uuid

# # Create your models here.
# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField(blank=True, null=True)
#     quantity = models.PositiveIntegerField(null=True)
#     # purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
#     sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    
#     def __str__(self) -> str:
#         return self.name
    
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


# inventory/models.py
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

CATEGORY = (
    ("Stationary", "Stationary"),
    ("Electronics", "Electronics"),
    ("Food", "Food"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    physical_address = models.CharField(max_length=40, null=True)
    mobile = models.CharField(max_length=12, null=True)
    picture = models.ImageField(default="avatar.jpeg", upload_to="Pictures")

    def __str__(self) -> str:
        return self.user.username


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY, null=True)
    quantity = models.PositiveIntegerField(null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created_by = models.ForeignKey(User, models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.product} ordered quantity {self.order_quantity}"

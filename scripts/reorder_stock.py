import os
import django

# Set up Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoInventory.settings")
django.setup()

from ..inventory.models import *
from django.db import transaction

def reorder_stock():
    # Iterate over products and check reorder levels
    with transaction.atomic():
        products_to_reorder = []
        products = Product.objects.all()

        for product in products:
            if product.quantity < product.reorder_level:
                products_to_reorder.append(product)

        for product in products_to_reorder:
            create_purchase_order(product)

def create_purchase_order(product):
    # Create a new purchase order
    purchase_order = PurchaseOrder.objects.create(
        vendor=product.preferred_vendor,
        warehouse=product.default_warehouse,
        delivery_date=desired_delivery_date,
    )

    # Create a purchase order product
    PurchaseOrderProduct.objects.create(
        purchase_order=purchase_order,
        product=product,
        unit_price=product.price,
        quantity=desired_order_quantity,
    )

if __name__ == '__main__':
    reorder_stock()

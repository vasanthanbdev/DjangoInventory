# Generated by Django 4.2.5 on 2023-10-07 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_item_remove_userprofile_user_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_number', models.CharField(max_length=50, unique=True)),
                ('bill_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(auto_now_add=True)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=50, unique=True)),
                ('invoice_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField(auto_now_add=True)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.customer')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PurchaseOrdernumber', models.CharField(max_length=50, unique=True)),
                ('order_date', models.DateField()),
                ('delivery_date', models.DateField()),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SalesOrdernumber', models.CharField(max_length=50, unique=True)),
                ('order_date', models.DateField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Closed', 'Closed')], max_length=100, null=True)),
                ('invoiced', models.BooleanField()),
                ('packed', models.BooleanField()),
                ('shipped', models.BooleanField()),
                ('delivery_date', models.DateField()),
                ('item_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Warehouse_number', models.CharField(max_length=50, unique=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(null=True)),
                ('contact', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='reorder_level',
            field=models.PositiveIntegerField(default=10),
        ),
        migrations.CreateModel(
            name='SalesOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('SalesOrder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.salesorder')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
            ],
        ),
        migrations.AddField(
            model_name='salesorder',
            name='items',
            field=models.ManyToManyField(through='inventory.SalesOrderItem', to='inventory.item'),
        ),
        migrations.CreateModel(
            name='PurchaseOrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
                ('purchase_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.purchaseorder')),
            ],
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='Vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.vendor'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='Warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='purchaseorder',
            name='items',
            field=models.ManyToManyField(through='inventory.PurchaseOrderItem', to='inventory.item'),
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Package_number', models.CharField(max_length=50, unique=True)),
                ('Package_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], max_length=100, null=True)),
                ('shippment_date', models.DateField()),
                ('quantity_ordered', models.PositiveIntegerField()),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.customer')),
                ('SalesOrder', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.salesorder')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.career')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.invoice')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='SalesOrder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.salesorder'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='items',
            field=models.ManyToManyField(through='inventory.InvoiceItem', to='inventory.item'),
        ),
        migrations.CreateModel(
            name='BillItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.PositiveIntegerField()),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.bill')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.item')),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='PurchaseOrder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.purchaseorder'),
        ),
        migrations.AddField(
            model_name='bill',
            name='Vendor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.vendor'),
        ),
        migrations.AddField(
            model_name='bill',
            name='Warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.warehouse'),
        ),
        migrations.AddField(
            model_name='bill',
            name='items',
            field=models.ManyToManyField(through='inventory.BillItem', to='inventory.item'),
        ),
    ]

# Generated by Django 4.2.5 on 2023-10-07 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_bill_career_customer_invoice_purchaseorder_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Career',
            new_name='Carrier',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='career',
            new_name='carrier',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='Customer',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='Package_date',
            new_name='package_date',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='SalesOrder',
            new_name='sales_order',
        ),
        migrations.RenameField(
            model_name='package',
            old_name='shippment_date',
            new_name='shipment_date',
        ),
        migrations.RemoveField(
            model_name='package',
            name='Package_number',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='Warehouse_number',
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_number',
            field=models.CharField(default='60F164AD2CA7', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.CharField(default='337D3CAB0F34', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='purchaseorder',
            name='PurchaseOrdernumber',
            field=models.CharField(default='8322032A17E9', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='salesorder',
            name='SalesOrdernumber',
            field=models.CharField(default='8DAA66435D90', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AddField(
            model_name='package',
            name='package_number',
            field=models.CharField(default='85CA2C51C4DC', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='warehouse',
            name='warehouse_number',
            field=models.CharField(default='45D1F0CD9187', max_length=50, unique=True),
        ),
    ]
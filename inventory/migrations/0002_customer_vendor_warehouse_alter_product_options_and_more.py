# Generated by Django 4.2.5 on 2023-10-15 06:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('contact', models.CharField(max_length=15, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('address', models.TextField(blank=True, null=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.RemoveField(
            model_name='product',
            name='purchase_price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='sale_price',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='reorder_level',
            field=models.PositiveIntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AddField(
            model_name='product',
            name='preferred_vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='inventory.vendor'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-09 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('customer_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('product_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('product_name', models.CharField(blank=True, max_length=20, null=True)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('unit', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Stores',
            fields=[
                ('store_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('store_name', models.CharField(blank=True, max_length=20, null=True)),
                ('desc', models.TextField()),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('supplier_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('supplier_name', models.CharField(blank=True, max_length=20, null=True)),
                ('address', models.CharField(blank=True, max_length=20, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('postal_code', models.IntegerField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=20, null=True)),
                ('phone', models.CharField(blank=True, max_length=12, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('order_detail_id', models.AutoField(editable=False, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('order_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.orders')),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.products')),
            ],
        ),
    ]
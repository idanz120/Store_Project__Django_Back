# Generated by Django 4.0.6 on 2022-08-10 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_products_store_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='product_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.products'),
        ),
    ]

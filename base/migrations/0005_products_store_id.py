# Generated by Django 4.0.6 on 2022-08-09 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_remove_stores_store_id_alter_stores_supplier_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='store_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.stores'),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-09 21:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_stores_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='stores',
            name='supplier_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.supplier'),
        ),
    ]

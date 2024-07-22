# Generated by Django 5.0.6 on 2024-07-22 02:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_baseinventory_remove_inventorypage_collection_and_more'),
        ('inventorytags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorylink',
            name='inventory',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='inventory.baseinventory'),
        ),
    ]
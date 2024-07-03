# Generated by Django 5.0.2 on 2024-07-03 21:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_rename_inventorycollection_inventory_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryCategory',
            fields=[
                ('inventory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.inventory')),
            ],
            options={
                'abstract': False,
            },
            bases=('inventory.inventory',),
        ),
        migrations.CreateModel(
            name='InventoryItem',
            fields=[
                ('inventory_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='inventory.inventory')),
            ],
            options={
                'abstract': False,
            },
            bases=('inventory.inventory',),
        ),
    ]

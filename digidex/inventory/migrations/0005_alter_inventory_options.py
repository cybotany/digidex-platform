# Generated by Django 5.0.6 on 2024-07-05 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_inventory_collection'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'verbose_name': 'inventory', 'verbose_name_plural': 'inventories'},
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-05 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventoryindex'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InventoryIndex',
            new_name='Index',
        ),
    ]

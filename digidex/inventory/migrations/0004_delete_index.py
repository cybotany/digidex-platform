# Generated by Django 5.0.6 on 2024-07-05 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_inventoryindex_index'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Index',
        ),
    ]

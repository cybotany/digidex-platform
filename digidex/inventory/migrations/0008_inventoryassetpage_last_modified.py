# Generated by Django 5.0.6 on 2024-08-05 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_remove_inventorylink_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventoryassetpage',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
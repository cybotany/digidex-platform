# Generated by Django 5.0.6 on 2024-07-29 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventorytags', '0002_remove_inventorylink_inventoryta_content_049509_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventorylink',
            name='link',
            field=models.URLField(blank=True, max_length=255, null=True),
        ),
    ]

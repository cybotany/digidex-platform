# Generated by Django 5.0.6 on 2024-07-29 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_userinventoryasset_created_at_and_more'),
        ('inventorytags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='inventorylink',
            name='inventoryta_content_049509_idx',
        ),
        migrations.RemoveIndex(
            model_name='inventorylink',
            name='inventoryta_object__9f38cf_idx',
        ),
        migrations.RemoveField(
            model_name='inventorylink',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='inventorylink',
            name='object_id',
        ),
        migrations.AddField(
            model_name='inventorylink',
            name='asset',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='inventory.userinventoryasset'),
        ),
        migrations.AlterField(
            model_name='inventorylink',
            name='link',
            field=models.URLField(default='https://digidex.tech', max_length=255),
        ),
        migrations.AddIndex(
            model_name='inventorylink',
            index=models.Index(fields=['asset'], name='inventoryta_asset_i_31049f_idx'),
        ),
    ]
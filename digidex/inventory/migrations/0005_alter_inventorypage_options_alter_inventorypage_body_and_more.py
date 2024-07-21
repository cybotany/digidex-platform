# Generated by Django 5.0.6 on 2024-07-21 20:37

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_inventoryindexpage_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventorypage',
            options={'verbose_name': 'inventory page', 'verbose_name_plural': 'inventorie pages'},
        ),
        migrations.AlterField(
            model_name='inventorypage',
            name='body',
            field=wagtail.fields.RichTextField(blank=True, null=True, verbose_name='body'),
        ),
        migrations.DeleteModel(
            name='InventoryIndexPage',
        ),
    ]
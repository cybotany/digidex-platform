# Generated by Django 5.0.6 on 2024-07-29 00:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('inventory', '0002_inventoryasset_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventorycategory',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.baseimage', verbose_name='icon'),
        ),
    ]

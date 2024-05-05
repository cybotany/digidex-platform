# Generated by Django 5.0.2 on 2024-05-02 17:10

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_rename_userdigitizedobjectindexpage_userdigitizedobjectinventorypage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdigitizedobject',
            name='user_inventory',
        ),
        migrations.AddField(
            model_name='userdigitizedobject',
            name='page',
            field=modelcluster.fields.ParentalKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='itemized_digits', to='inventory.userdigitizedobjectinventorypage'),
            preserve_default=False,
        ),
    ]
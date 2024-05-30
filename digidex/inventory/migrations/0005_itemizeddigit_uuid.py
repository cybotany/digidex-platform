# Generated by Django 5.0.2 on 2024-05-28 22:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_remove_itemizeddigitpage_digit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemizeddigit',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='Inventory Category UUID'),
        ),
    ]
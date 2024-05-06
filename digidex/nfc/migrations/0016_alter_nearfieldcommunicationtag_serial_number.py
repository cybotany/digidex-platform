# Generated by Django 5.0.2 on 2024-05-06 21:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfc', '0015_alter_nearfieldcommunicationtag_serial_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='serial_number',
            field=models.CharField(db_index=True, max_length=32, unique=True),
        ),
    ]

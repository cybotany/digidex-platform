# Generated by Django 5.0.2 on 2024-07-01 05:08

import nfc.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfc', '0008_alter_nearfieldcommunicationlink_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='serial_number',
            field=models.CharField(db_index=True, editable=False, max_length=32, unique=True, validators=[nfc.validators.validate_ntag_serial]),
        ),
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True),
        ),
    ]

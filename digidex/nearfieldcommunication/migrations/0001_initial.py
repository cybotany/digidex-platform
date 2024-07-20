# Generated by Django 5.0.6 on 2024-07-18 15:34

import inventory.validators
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NearFieldCommunicationTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('serial_number', models.CharField(db_index=True, editable=False, max_length=32, unique=True, validators=[inventory.validators.validate_ntag_serial])),
                ('tag_form', models.CharField(choices=[('PL', 'Plant Label'), ('DT', 'Dog Tag'), ('CT', 'Cat Tag'), ('BS', 'Bubble Sticker'), ('RS', 'Regular Sticker'), ('WI', 'Wet Inlay'), ('DI', 'Dry Inlay')], default='RS', max_length=2)),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'nfc tag',
                'verbose_name_plural': 'nfc tags',
            },
        ),
    ]

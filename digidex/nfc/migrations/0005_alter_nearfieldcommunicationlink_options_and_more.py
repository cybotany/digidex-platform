# Generated by Django 5.0.2 on 2024-07-01 02:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfc', '0004_alter_nearfieldcommunicationlink_content_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nearfieldcommunicationlink',
            options={'verbose_name': 'NFC Link', 'verbose_name_plural': 'NFC Links'},
        ),
        migrations.AlterModelOptions(
            name='nearfieldcommunicationtag',
            options={'verbose_name': 'NFC Tag', 'verbose_name_plural': 'NFC Tags'},
        ),
        migrations.RemoveField(
            model_name='nearfieldcommunicationlink',
            name='sort_order',
        ),
        migrations.AddField(
            model_name='nearfieldcommunicationtag',
            name='ntag_type',
            field=models.CharField(choices=[('PL', 'Plant Label'), ('DT', 'Dog Tag'), ('CT', 'Cat Tag'), ('BS', 'Bubble Sticker'), ('RS', 'Regular Sticker'), ('WI', 'Wet Inlay'), ('DI', 'Dry Inlay')], default='RS', max_length=2),
        ),
        migrations.AlterField(
            model_name='nearfieldcommunicationlink',
            name='tag',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='mapping', to='nfc.nearfieldcommunicationtag'),
        ),
    ]

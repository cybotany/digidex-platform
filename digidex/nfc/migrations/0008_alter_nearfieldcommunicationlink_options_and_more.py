# Generated by Django 5.0.2 on 2024-07-01 03:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfc', '0007_rename_ntag_type_nearfieldcommunicationtag_tag_form_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='nearfieldcommunicationlink',
            options={'verbose_name': 'nfc mapping', 'verbose_name_plural': 'nfc mappings'},
        ),
        migrations.AlterModelOptions(
            name='nearfieldcommunicationtag',
            options={'verbose_name': 'nfc tag', 'verbose_name_plural': 'nfc tags'},
        ),
    ]

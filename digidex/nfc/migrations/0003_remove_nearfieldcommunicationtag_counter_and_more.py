# Generated by Django 5.0.2 on 2024-04-28 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nfc', '0002_alter_nearfieldcommunicationtag_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nearfieldcommunicationtag',
            name='counter',
        ),
        migrations.RemoveField(
            model_name='nearfieldcommunicationtag',
            name='eeprom',
        ),
    ]
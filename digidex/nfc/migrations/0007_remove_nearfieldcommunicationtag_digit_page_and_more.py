# Generated by Django 5.0.2 on 2024-04-29 20:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0010_digitregistrationformpage_alter_userpage_options_and_more'),
        ('nfc', '0006_rename_digit_nearfieldcommunicationtag_digit_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nearfieldcommunicationtag',
            name='digit_page',
        ),
        migrations.AddField(
            model_name='nearfieldcommunicationtag',
            name='digit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nfc_tags', to='inventory.digit', verbose_name='Digital Object'),
        ),
    ]
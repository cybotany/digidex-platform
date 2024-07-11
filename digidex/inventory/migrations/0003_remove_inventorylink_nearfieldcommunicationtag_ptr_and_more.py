# Generated by Django 5.0.6 on 2024-07-11 22:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_inventorylink'),
        ('nearfieldcommunication', '0001_initial'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorylink',
            name='nearfieldcommunicationtag_ptr',
        ),
        migrations.AlterField(
            model_name='inventorylink',
            name='resource',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.page'),
        ),
    ]
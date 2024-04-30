# Generated by Django 5.0.2 on 2024-04-29 22:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_remove_digit_user_remove_digitpage_user_and_more'),
        ('nfc', '0008_alter_nearfieldcommunicationtag_digit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='digit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ntag', to='inventory.digit'),
        ),
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='last_modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='serial_number',
            field=models.CharField(db_index=True, max_length=32, unique=True),
        ),
    ]

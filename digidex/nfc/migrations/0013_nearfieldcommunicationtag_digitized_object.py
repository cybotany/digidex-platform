# Generated by Django 5.0.2 on 2024-05-04 23:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digitization', '0003_alter_digitizedobject_description_and_more'),
        ('nfc', '0012_remove_nearfieldcommunicationtag_digit'),
    ]

    operations = [
        migrations.AddField(
            model_name='nearfieldcommunicationtag',
            name='digitized_object',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ntag', to='digitization.digitizedobject'),
        ),
    ]
# Generated by Django 4.2.6 on 2024-01-13 06:08

import digit.utils.custom_storage
from journal.models import journal_entry_directory_path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='image',
            field=models.ImageField(blank=True, help_text='(Optional) The image to save with the journal entry. Only .jpg, .png, and .jpeg extensions are allowed.', null=True, storage=digit.utils.custom_storage.PrivateMediaStorage(), upload_to=journal_entry_directory_path),
        ),
    ]

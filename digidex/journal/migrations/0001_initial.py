# Generated by Django 4.2.6 on 2024-01-27 05:18

import digidex.journal.models.collection
import digidex.journal.models.entry
import digidex.utils.custom_storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, help_text='Thumbnail image for the digitized plant.', null=True, upload_to=digidex.journal.models.collection.thumbnail_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the journal collection instance was created.', verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, help_text='The date and time when the journal collection instance was last modified.', verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Journal Collection',
                'verbose_name_plural': 'Journal Collections',
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watered', models.BooleanField(default=False, help_text='Indicates whether the digitized plant was watered in this journal entry.', verbose_name='Watered')),
                ('fertilized', models.BooleanField(default=False, help_text='Indicates whether the digitized plant was fertilized in this journal entry.', verbose_name='Fertilized')),
                ('cleaned', models.BooleanField(default=False, help_text='Indicates whether the digitized plant was cleaned in this journal entry.', verbose_name='Cleaned')),
                ('content', models.TextField(blank=True, help_text='The textual content of the journal entry.', null=True, verbose_name='Content')),
                ('image', models.ImageField(blank=True, help_text='(Optional) The image to save with the journal entry. Only .jpg, .png, and .jpeg extensions are allowed.', null=True, storage=digidex.utils.custom_storage.PrivateMediaStorage(), upload_to=digidex.journal.models.entry.journal_image_directory_path)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when this journal entry was created.', verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, help_text='The date and time when this journal entry was last modified.', verbose_name='Last Modified')),
                ('collection', models.ForeignKey(help_text='The collection to which this journal entry belongs.', on_delete=django.db.models.deletion.CASCADE, related_name='journal_entries', to='journal.collection')),
            ],
            options={
                'verbose_name': 'Journal Entry',
                'verbose_name_plural': 'Journal Entries',
                'ordering': ['-created_at'],
            },
        ),
    ]

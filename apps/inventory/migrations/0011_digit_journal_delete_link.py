# Generated by Django 4.2.6 on 2024-01-02 00:23

import apps.utils.custom_storage
import apps.utils.helpers.get_path
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taxonomy', '0010_alter_geographicdivision_tsn_alter_hierarchy_tsn_and_more'),
        ('inventory', '0010_remove_link_group_delete_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Digit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='A human-readable name for the digitized plant.', max_length=50, null=True)),
                ('description', models.TextField(blank=True, help_text='A short description of the digitized plant.', max_length=500, null=True)),
                ('taxonomic_unit', models.ForeignKey(blank=True, help_text='The taxonomic classification of the digitized plant.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='digits', to='taxonomy.unit')),
            ],
            options={
                'verbose_name': 'Digit',
                'verbose_name_plural': 'Digits',
            },
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when this journal entry was created.', verbose_name='Created At')),
                ('entry', models.TextField(help_text='The textual content of the journal entry.', verbose_name='Content')),
                ('image', models.ImageField(blank=True, help_text='(Optional) The image to save with the journal entry. Only .jpg, .png, and .jpeg extensions are allowed.', null=True, upload_to=apps.utils.custom_storage.JournalImageStorage(apps.utils.helpers.get_path.get_user_directory_path))),
                ('digit', models.ForeignKey(help_text='The digitized plant to which this journal entry is related.', on_delete=django.db.models.deletion.CASCADE, related_name='journal_entries', to='inventory.digit')),
                ('user', models.ForeignKey(help_text='The user who created this journal entry.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Journal Entry',
                'verbose_name_plural': 'Journal Entries',
                'ordering': ['-created_at'],
            },
        ),
        migrations.DeleteModel(
            name='Link',
        ),
    ]

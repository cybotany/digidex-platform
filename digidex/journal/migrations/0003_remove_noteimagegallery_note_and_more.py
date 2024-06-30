# Generated by Django 5.0.2 on 2024-06-28 23:20

import django.db.models.deletion
import uuid
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('journal', '0002_note_content_type_note_object_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noteimagegallery',
            name='note',
        ),
        migrations.RemoveField(
            model_name='noteimagegallery',
            name='image',
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('entry', wagtail.fields.RichTextField(blank=True, null=True)),
                ('object_id', models.PositiveIntegerField(db_index=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.digideximage')),
            ],
        ),
        migrations.DeleteModel(
            name='Note',
        ),
        migrations.DeleteModel(
            name='NoteImageGallery',
        ),
    ]
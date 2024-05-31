# Generated by Django 5.0.2 on 2024-05-31 16:17

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DigitalObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='Digitized Object UUID')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='Digitized Object Slug')),
                ('name', models.CharField(help_text='Digitized Object Name.', max_length=100, null=True)),
                ('description', models.TextField(blank=True, help_text='Digitized Object Description.', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

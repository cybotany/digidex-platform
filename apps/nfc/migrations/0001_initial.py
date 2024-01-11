# Generated by Django 4.2.6 on 2024-01-11 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.CharField(db_index=True, help_text='The unique serial number associated with the NFC tag.', max_length=8, unique=True, verbose_name='Tag Serial Number')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, help_text='The unique identifier associated with the NFC tag or identification mechanism.', unique=True, verbose_name='Tag UUID')),
                ('counter', models.IntegerField(default=0, help_text='The number of times the tag has been scanned.', verbose_name='Counter')),
                ('active', models.BooleanField(default=False, help_text='Indicates whether the link is currently active and mapped to a digital object.', verbose_name='Active')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the link instance was created.', verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, help_text='The date and time when the link instance was last modified.', verbose_name='Last Modified')),
                ('user', models.ForeignKey(blank=True, help_text='The user associated with this link.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Link',
                'verbose_name_plural': 'Links',
            },
        ),
    ]

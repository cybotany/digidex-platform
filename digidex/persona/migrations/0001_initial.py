# Generated by Django 5.0.2 on 2024-03-22 00:29

import digidex.utils.storage
import django.db.models.deletion
import persona.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DigiDexProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(editable=False, help_text='Slugified version of the username for URL usage.', max_length=255, unique=True)),
                ('bio', models.TextField(blank=True, help_text='A short biography of the user.', max_length=500)),
                ('location', models.CharField(blank=True, help_text='The location of the user.', max_length=30)),
                ('avatar', models.ImageField(blank=True, help_text='The avatar image of the profile.', null=True, storage=digidex.utils.storage.PublicMediaStorage, upload_to=persona.models.profile_avatar_directory_path)),
                ('is_public', models.BooleanField(default=False, help_text='Indicates if the profile should be publicly visible to the public or private. Profile is private by default.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the profile was created.', verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, help_text='The date and time when the profile was last modified.', verbose_name='Last Modified')),
                ('user', models.OneToOneField(help_text='The user associated with this profile.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]

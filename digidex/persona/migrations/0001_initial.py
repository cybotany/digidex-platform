# Generated by Django 5.0.2 on 2024-03-22 08:23

import base.blocks.basics
import base.fields.django
import base.fields.wagtail
import base.utils.storage
import django.db.models.deletion
import persona.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', base.fields.wagtail.BaseStreamField([('paragraph', base.blocks.basics.BaseRichTextBlock())], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DigiDexProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', base.fields.django.BaseSlugField(editable=False, help_text='Slugified version of the username for URL usage.', max_length=255, unique=True)),
                ('bio', base.fields.django.BaseTextField(blank=True, help_text='A short biography of the user.', max_length=500)),
                ('location', base.fields.django.BaseCharField(blank=True, help_text='The location of the user.', max_length=30)),
                ('avatar', base.fields.django.BaseImageField(blank=True, help_text='The avatar image of the profile.', null=True, storage=base.utils.storage.PublicMediaStorage, upload_to=persona.models.profile_avatar_directory_path)),
                ('is_public', base.fields.django.BaseBooleanField(default=False, help_text='Indicates if the profile should be publicly visible to the public or private. Profile is private by default.')),
                ('created_at', base.fields.django.BaseDateTimeField(auto_now_add=True, help_text='The date and time when the profile was created.', verbose_name='Created At')),
                ('last_modified', base.fields.django.BaseDateTimeField(auto_now=True, help_text='The date and time when the profile was last modified.', verbose_name='Last Modified')),
                ('user', base.fields.django.BaseOneToOneField(help_text='The user associated with this profile.', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]

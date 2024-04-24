# Generated by Django 5.0.2 on 2024-04-24 02:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='A short biography of the user.', max_length=500)),
                ('location', models.CharField(blank=True, help_text='The location of the user.', max_length=30)),
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
        migrations.CreateModel(
            name='UserProfilePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('bio', models.TextField(blank=True, help_text='A short biography of the user.', max_length=500)),
                ('location', models.CharField(blank=True, help_text='The location of the user.', max_length=30)),
                ('is_public', models.BooleanField(default=False, help_text='Indicates if the profile should be publicly visible.')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('user', models.OneToOneField(help_text='The user associated with this profile.', on_delete=django.db.models.deletion.CASCADE, related_name='profile_page', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
                'verbose_name_plural': 'User Profiles',
            },
            bases=('wagtailcore.page',),
        ),
    ]

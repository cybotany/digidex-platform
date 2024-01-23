# Generated by Django 4.2.6 on 2024-01-11 20:58

import digit.utils.custom_storage
import digit.utils.validators
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
from digit.accounts.models import profile_avatar_directory_path
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, help_text='The universal unique identifier associated with each User.', unique=True, verbose_name='User UUID')),
                ('email_confirmed', models.BooleanField(default=False, help_text='Indicates whether the user has confirmed their email address.')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, help_text='A short biography of the user.', max_length=500)),
                ('location', models.CharField(blank=True, help_text='The location of the user.', max_length=30)),
                ('avatar', models.ImageField(blank=True, help_text='The profile picture of the user.', null=True, storage=digit.utils.custom_storage.PublicMediaStorage(), upload_to=profile_avatar_directory_path, validators=[digit.utils.validators.validate_profile_avatar])),
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
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(choices=[('plant', 'Plant')], help_text='Type of the item involved in the activity, such as "plant" or "cea".', max_length=25)),
                ('activity_status', models.CharField(choices=[('register', 'Registered'), ('update', 'Updated'), ('delete', 'Deleted')], help_text='Nature of the activity (e.g., "created", "updated", "deleted").', max_length=20)),
                ('content', models.TextField(help_text='Detailed description of the activity.')),
                ('timestamp', models.DateTimeField(auto_now_add=True, help_text='The date and time when the activity was recorded.')),
                ('user', models.ForeignKey(help_text='Reference to the user who performed the activity.', on_delete=django.db.models.deletion.CASCADE, related_name='recent_activities', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]

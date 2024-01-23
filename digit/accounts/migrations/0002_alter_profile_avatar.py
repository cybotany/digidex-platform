# Generated by Django 4.2.6 on 2024-01-22 04:36

import digit.accounts.models.profile
import digit.utils.custom_storage
import digit.utils.validators.profile_avatar_validator
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, help_text='The avatar image of the profile.', null=True, storage=digit.utils.custom_storage.PublicMediaStorage(), upload_to=digit.accounts.models.profile.profile_avatar_directory_path, validators=[digit.utils.validators.profile_avatar_validator.validate_profile_avatar]),
        ),
    ]

# Generated by Django 5.0.2 on 2024-05-19 01:29

import base.utils.storage
import profiles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, storage=base.utils.storage.PublicMediaStorage(), upload_to=profiles.models.user_avatar_path),
        ),
    ]

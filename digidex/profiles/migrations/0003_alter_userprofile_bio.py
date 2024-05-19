# Generated by Django 5.0.2 on 2024-05-19 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True, help_text='Short Biography about the user.', null=True),
        ),
    ]

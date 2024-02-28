# Generated by Django 4.2.9 on 2024-02-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_rename_username_slug_user_slug_delete_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='slug',
            field=models.SlugField(editable=False, help_text='Slugified version of the username for URL usage.', max_length=255, unique=True),
        ),
    ]

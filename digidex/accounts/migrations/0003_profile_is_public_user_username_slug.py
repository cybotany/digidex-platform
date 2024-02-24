# Generated by Django 4.2.9 on 2024-02-22 22:27

from django.db import migrations, models
from django.utils.text import slugify

def generate_username_slugs(apps, schema_editor):
    User = apps.get_model('accounts', 'User')  
    for user in User.objects.all():
        user.username_slug = slugify(user.username)
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_delete_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='is_public',
            field=models.BooleanField(default=False, help_text='Indicates if the profile should be publicly visible or private.'),
        ),
        migrations.AddField(
            model_name='user',
            name='username_slug',
            field=models.SlugField(editable=False, help_text='Slugified version of the username for URL usage.', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]

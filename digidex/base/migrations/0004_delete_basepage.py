# Generated by Django 5.0.2 on 2024-03-27 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_footernavigationsettings_linkedin_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BasePage',
        ),
    ]
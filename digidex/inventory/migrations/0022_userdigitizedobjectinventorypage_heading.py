# Generated by Django 5.0.2 on 2024-05-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0021_alter_userdigitizedobject_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdigitizedobjectinventorypage',
            name='heading',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
# Generated by Django 5.0.2 on 2024-04-23 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homepagesection'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagesection',
            name='style',
        ),
    ]
# Generated by Django 5.0.6 on 2024-08-04 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_homepage_primary_cta_text_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='collection',
        ),
    ]

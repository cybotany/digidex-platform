# Generated by Django 5.0.2 on 2024-05-18 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_homepage_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='hero_cta_link',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='hero_cta_text',
        ),
    ]

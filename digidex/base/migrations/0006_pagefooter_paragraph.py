# Generated by Django 5.0.2 on 2024-04-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_rename_headeradvertisement_advertbanner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagefooter',
            name='paragraph',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]
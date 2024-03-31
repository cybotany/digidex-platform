# Generated by Django 5.0.2 on 2024-03-31 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_blogpage_authors_remove_blogpage_page_ptr_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='heading_paragraph',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='heading_title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
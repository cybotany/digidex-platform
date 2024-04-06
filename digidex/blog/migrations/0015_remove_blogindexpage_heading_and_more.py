# Generated by Django 5.0.2 on 2024-04-04 02:44

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_blogtagindexpage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='heading',
        ),
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.StreamField([('page_heading', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock()), ('introduction', wagtail.blocks.RichTextBlock())]))], blank=True, null=True),
        ),
    ]
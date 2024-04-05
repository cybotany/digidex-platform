# Generated by Django 5.0.2 on 2024-04-05 00:52

import base.blocks.basic
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_blogindexpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.StreamField([('page_heading', wagtail.blocks.StructBlock([('heading', base.blocks.basic.Heading(required=True)), ('introduction', base.blocks.basic.Paragraph(required=False))]))], blank=True, null=True),
        ),
    ]

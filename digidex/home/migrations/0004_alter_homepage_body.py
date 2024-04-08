# Generated by Django 5.0.2 on 2024-04-08 14:35

import base.blocks
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_homepage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('information', wagtail.blocks.StructBlock([('text', base.blocks.BasicTextBlock()), ('icon', base.blocks.BasicImageBlock()), ('link', base.blocks.BasicInternalLinkBlock())])), ('heading', wagtail.blocks.StructBlock([('text', base.blocks.BasicCharBlock(required=True)), ('size', base.blocks.BasicCharBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False))])), ('paragraph', base.blocks.BasicParagraphBlock())]))], blank=True, null=True),
        ),
    ]

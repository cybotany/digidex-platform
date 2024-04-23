# Generated by Django 5.0.2 on 2024-04-08 03:43

import base.blocks
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('text', base.blocks.BasicCharBlock(required=True)), ('size', base.blocks.BasicCharBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('style', base.blocks.BasicCharBlock(default='heading', required=False))])), ('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(required=True)), ('style', base.blocks.BasicCharBlock(default='paragraph', required=False))])), ('button', wagtail.blocks.StructBlock([('page', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(help_text='Select an internal page to link to.', required=False)), ('style', base.blocks.BasicCharBlock(blank=True, default='link', required=False))])), ('url', wagtail.blocks.StructBlock([('url', wagtail.blocks.URLBlock(help_text='Select an external URL to link to.', required=False)), ('style', base.blocks.BasicCharBlock(blank=True, default='link', required=False))])), ('cta', base.blocks.BasicCharBlock())])), ('icon_button', wagtail.blocks.StructBlock([('page', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(help_text='Select an internal page to link to.', required=False)), ('style', base.blocks.BasicCharBlock(blank=True, default='link', required=False))])), ('url', wagtail.blocks.StructBlock([('url', wagtail.blocks.URLBlock(help_text='Select an external URL to link to.', required=False)), ('style', base.blocks.BasicCharBlock(blank=True, default='link', required=False))])), ('cta', wagtail.blocks.StructBlock([('content', wagtail.blocks.TextBlock()), ('style', base.blocks.BasicCharBlock(blank=True, default='text', required=False))])), ('icon', wagtail.blocks.StructBlock([('icon', base.blocks.BasicImageBlock(help_text='Select an icon for the info block', required=True)), ('style', base.blocks.BasicCharBlock(blank=True, default='icon', required=False))]))]))], blank=True, null=True),
        ),
    ]
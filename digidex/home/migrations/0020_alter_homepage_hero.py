# Generated by Django 5.0.2 on 2024-04-06 00:48

import base.blocks.basic
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_homepage_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('classname', wagtail.blocks.CharBlock(default='heading', help_text='CSS class for styling', required=False))])), ('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(required=True)), ('classname', wagtail.blocks.CharBlock(default='paragraph', help_text='CSS class for styling', required=False))])), ('button', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=True)), ('text', wagtail.blocks.CharBlock(required=False))])), ('icon_button', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=True)), ('text', wagtail.blocks.CharBlock(required=False)), ('icon', base.blocks.basic.ImageBlock(required=True))]))], blank=True, null=True),
        ),
    ]
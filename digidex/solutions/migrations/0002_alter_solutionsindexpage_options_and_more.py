# Generated by Django 5.0.2 on 2024-04-01 02:24

import base.blocks.basic
import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='solutionsindexpage',
            options={'verbose_name': 'Solutions Index Page', 'verbose_name_plural': 'Solutions Index Pages'},
        ),
        migrations.AddField(
            model_name='solutionsindexpage',
            name='features',
            field=wagtail.fields.StreamField([('feature', wagtail.blocks.StructBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')], required=False))], help_text='Enter the heading text here', max_length=50)), ('paragraph', base.blocks.basic.ParagraphBlock(help_text='Enter the body here', required=False))], help_text='Feature sections'))], blank=True, help_text='Feature sections', null=True),
        ),
        migrations.AddField(
            model_name='solutionsindexpage',
            name='solutions',
            field=wagtail.fields.StreamField([('solution', wagtail.blocks.StructBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')], required=False))], help_text='Enter the heading text here', max_length=50)), ('paragraph', base.blocks.basic.ParagraphBlock(help_text='Enter the body here', required=False)), ('linked_page', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')], required=False))])), ('body', base.blocks.basic.ParagraphBlock()), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks', icon='media'))], help_text='Link to a page', required=False))], help_text='Solution sections'))], blank=True, help_text='Solution sections', null=True),
        ),
    ]

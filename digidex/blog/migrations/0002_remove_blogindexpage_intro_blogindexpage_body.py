# Generated by Django 5.0.2 on 2024-03-31 07:14

import wagtail.blocks
import wagtail.embeds.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')], required=False))])), ('paragraph', wagtail.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('caption', wagtail.blocks.CharBlock(required=False)), ('attribution', wagtail.blocks.CharBlock(required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(help_text='Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks', icon='media'))], blank=True),
        ),
    ]

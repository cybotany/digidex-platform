# Generated by Django 5.0.2 on 2024-04-01 15:35

import base.blocks.basic.image
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0002_alter_solutionsindexpage_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solutionsindexpage',
            name='solutions',
            field=wagtail.fields.StreamField([('solution', wagtail.blocks.StructBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='title', required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5')], required=False))], help_text='Enter the heading text here', max_length=50)), ('paragraph', base.blocks.basic.image.ParagraphBlock(help_text='Enter the body here', required=False))], help_text='Solution sections'))], blank=True, help_text='Solution sections', null=True),
        ),
    ]

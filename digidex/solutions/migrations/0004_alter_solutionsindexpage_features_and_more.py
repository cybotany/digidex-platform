# Generated by Django 5.0.2 on 2024-04-01 23:02

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0003_alter_solutionsindexpage_solutions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solutionsindexpage',
            name='features',
            field=wagtail.fields.StreamField([('feature', wagtail.blocks.StructBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='heading', required=True))], help_text='Enter the heading text here', max_length=50)), ('paragraph', wagtail.blocks.StructBlock([('paragraph', wagtail.blocks.RichTextBlock(form_classname='paragraph', required=True))], help_text='Enter the body here', required=False))], help_text='Feature sections'))], blank=True, help_text='Feature sections', null=True),
        ),
        migrations.AlterField(
            model_name='solutionsindexpage',
            name='solutions',
            field=wagtail.fields.StreamField([('solution', wagtail.blocks.StructBlock([('heading', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='heading', required=True))], help_text='Enter the heading text here', max_length=50)), ('paragraph', wagtail.blocks.StructBlock([('paragraph', wagtail.blocks.RichTextBlock(form_classname='paragraph', required=True))], help_text='Enter the body here', required=False))], help_text='Solution sections'))], blank=True, help_text='Solution sections', null=True),
        ),
    ]
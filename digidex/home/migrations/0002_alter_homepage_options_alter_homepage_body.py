# Generated by Django 5.0.2 on 2024-03-27 01:36

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'Homepage'},
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.fields.StreamField([('section', wagtail.blocks.StructBlock([('section_type', wagtail.blocks.ChoiceBlock(choices=[('company', 'Company'), ('contact', 'Contact'), ('regular', 'Regular')], help_text='Select the type of section')), ('content', wagtail.blocks.StreamBlock([('heading', wagtail.blocks.CharBlock(form_classname='full title')), ('paragraph', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]))]))], blank=True, null=True),
        ),
    ]
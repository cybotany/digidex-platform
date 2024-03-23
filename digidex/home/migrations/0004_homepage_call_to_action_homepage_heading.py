# Generated by Django 5.0.2 on 2024-03-23 08:42

import base.blocks.basics
import base.fields.wagtail
import wagtail.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_homepage_solutions'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='call_to_action',
            field=base.fields.wagtail.BaseStreamField([('cta', wagtail.blocks.StructBlock([('text', base.blocks.basics.BaseCharBlock()), ('button', wagtail.blocks.StructBlock([('text', base.blocks.basics.BaseCharBlock(help_text='Enter the link title', required=False)), ('url', base.blocks.basics.BaseURLBlock(help_text='Enter the URL', required=False)), ('target', wagtail.blocks.ChoiceBlock(choices=[('_self', 'Same window'), ('_blank', 'New window')], help_text='Where the link should open', required=False))]))]))], null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='heading',
            field=base.fields.wagtail.BaseStreamField([('heading', wagtail.blocks.StructBlock([('title', base.blocks.basics.BaseCharBlock(help_text='Enter the heading title', required=True)), ('text', base.blocks.basics.BaseTextBlock(help_text='Enter the heading text', required=True))]))], null=True),
        ),
    ]

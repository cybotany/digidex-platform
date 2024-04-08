# Generated by Django 5.0.2 on 2024-04-07 13:38

import base.blocks
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.StreamField([('hero', wagtail.blocks.StructBlock([('information', wagtail.blocks.StructBlock([('text', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.CharBlock(blank=True, default='text', required=False))])), ('icon', wagtail.blocks.StructBlock([('icon', base.blocks.BasicImageBlock(help_text='Select an icon for the info block', required=True)), ('style', wagtail.blocks.CharBlock(blank=True, default='icon', required=False))])), ('link', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(help_text='Select an internal page to link to.', required=False)), ('style', wagtail.blocks.CharBlock(blank=True, default='link', required=False))]))])), ('heading', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('size', wagtail.blocks.ChoiceBlock(blank=True, choices=[('', 'Select a heading size'), ('h1', 'H1'), ('h2', 'H2'), ('h3', 'H3'), ('h4', 'H4'), ('h5', 'H5'), ('h6', 'H6')], required=False)), ('style', wagtail.blocks.CharBlock(default='heading', required=False))])), ('paragraph', wagtail.blocks.StructBlock([('text', wagtail.blocks.TextBlock(required=True)), ('style', wagtail.blocks.CharBlock(default='paragraph', required=False))])), ('cta', wagtail.blocks.StructBlock([('page', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(help_text='Select an internal page to link to.', required=False)), ('style', wagtail.blocks.CharBlock(blank=True, default='link', required=False))])), ('text', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(required=True)), ('style', wagtail.blocks.CharBlock(blank=True, default='text', required=False))])), ('style', wagtail.blocks.CharBlock(blank=True, default='text', required=False))]))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Home Page',
                'verbose_name_plural': 'Home Pages',
            },
            bases=('wagtailcore.page',),
        ),
    ]

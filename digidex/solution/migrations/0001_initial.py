# Generated by Django 5.0.2 on 2024-03-22 07:00

import base.blocks.basic_blocks
import base.fields.wagtail_fields
import django.db.models.deletion
import wagtail.blocks
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='SolutionIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('introduction', base.fields.wagtail_fields.BaseStreamField([('paragraph', base.blocks.basic_blocks.BaseRichTextBlock())], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SolutionsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('top_section', base.fields.wagtail_fields.BaseStreamField([('heading', base.blocks.basic_blocks.BaseCharBlock(form_classname='full title')), ('paragraph', base.blocks.basic_blocks.BaseRichTextBlock())], blank=True, null=True)),
                ('about_sections', base.fields.wagtail_fields.BaseStreamField([('about_section', wagtail.blocks.StructBlock([('icon', base.blocks.basic_blocks.BaseImageBlock(required=True)), ('title', base.blocks.basic_blocks.BaseCharBlock(required=True)), ('text', base.blocks.basic_blocks.BaseTextBlock(required=True))]))], blank=True, null=True)),
                ('quote', base.fields.wagtail_fields.BaseStreamField([('quote', wagtail.blocks.StructBlock([('quote_text', base.blocks.basic_blocks.BaseTextBlock(required=True)), ('author_name', base.blocks.basic_blocks.BaseCharBlock(required=True)), ('author_role', base.blocks.basic_blocks.BaseCharBlock(required=True)), ('author_signature', base.blocks.basic_blocks.BaseImageBlock(required=False))]))], blank=True, null=True)),
                ('team_members', base.fields.wagtail_fields.BaseStreamField([('team_member', wagtail.blocks.StructBlock([('image', base.blocks.basic_blocks.BaseImageBlock(required=True)), ('name', base.blocks.basic_blocks.BaseCharBlock(required=True)), ('role', base.blocks.basic_blocks.BaseCharBlock(required=True))]))], blank=True, null=True)),
                ('reviews', base.fields.wagtail_fields.BaseStreamField([('review', wagtail.blocks.StructBlock([('reviewer_name', base.blocks.basic_blocks.BaseCharBlock(required=True)), ('review_text', base.blocks.basic_blocks.BaseTextBlock(required=True)), ('star_rating', base.blocks.basic_blocks.BaseIntegerBlock(max_value=5, min_value=1, required=True))]))], blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
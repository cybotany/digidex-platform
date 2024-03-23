# Generated by Django 5.0.2 on 2024-03-23 03:37

import base.blocks.basics
import base.fields.wagtail
import wagtail.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='hero_cta',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='hero_cta_link',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='hero_heading',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='hero_text',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='lottie',
        ),
        migrations.AddField(
            model_name='homepage',
            name='hero',
            field=base.fields.wagtail.BaseStreamField([('hero', wagtail.blocks.StructBlock([('heading', base.blocks.basics.BaseCharBlock(max_length=255, required=True)), ('sub_heading', base.blocks.basics.BaseTextBlock(required=False)), ('image', base.blocks.basics.BaseImageBlock(required=False)), ('cta', wagtail.blocks.StructBlock([('text', base.blocks.basics.BaseCharBlock(max_length=255, required=True)), ('url', base.blocks.basics.BaseURLBlock(required=True))]))]))], blank=True, null=True),
        ),
        migrations.AddField(
            model_name='homepage',
            name='solutions',
            field=base.fields.wagtail.BaseStreamField([('solutions', wagtail.blocks.StructBlock([('content', wagtail.blocks.StructBlock([('subcontent', wagtail.blocks.StreamBlock([('solutions', wagtail.blocks.StructBlock([('items', base.blocks.basics.BaseListBlock(wagtail.blocks.StructBlock([('tag', wagtail.blocks.StructBlock([('text', base.blocks.basics.BaseCharBlock(help_text="Enter the text for the tag (e.g., 'Most popular').", required=True)), ('color', wagtail.blocks.ChoiceBlock(choices=[('yellow', 'Yellow'), ('blue', 'Blue')], help_text='Select the color of the tag.'))], help_text="Optionally add a tag to the card, such as 'Most popular' or 'New'.", required=False)), ('content', wagtail.blocks.StructBlock([('text', base.blocks.basics.BaseCharBlock(help_text='Enter the link title', required=False)), ('url', base.blocks.basics.BaseURLBlock(help_text='Enter the URL', required=False)), ('target', wagtail.blocks.ChoiceBlock(choices=[('_self', 'Same window'), ('_blank', 'New window')], help_text='Where the link should open', required=False)), ('icon', base.blocks.basics.BaseImageBlock(help_text='Optional: Select an icon image', required=False)), ('image', base.blocks.basics.BaseImageBlock(help_text='Select an image for the solution card.', required=True)), ('heading', base.blocks.basics.BaseRichTextBlock(help_text='Enter the heading for the solution card.', required=True)), ('paragraph', base.blocks.basics.BaseRichTextBlock(help_text='Enter a descriptive paragraph for the solution.', required=True))], help_text='Add the main content for the card.')), ('button', wagtail.blocks.StructBlock([('text', base.blocks.basics.BaseCharBlock(help_text='Enter the text for the link.', required=True)), ('url', base.blocks.basics.BaseURLBlock(help_text='Enter the URL', required=False)), ('target', wagtail.blocks.ChoiceBlock(choices=[('_self', 'Open in the same window'), ('_blank', 'Open in a new window')], help_text='Choose where the link should open.')), ('icon', base.blocks.basics.BaseImageBlock(help_text='Select an icon image to represent the link.', required=True)), ('page', base.blocks.basics.BasePageBlock(help_text='Select the destination page for the link.', required=False))], help_text='Define an icon with a link for additional details or actions.', required=True))]), help_text='Add up to 4 solution cards. Each card will be displayed in a single row.', max_num=4, min_num=1))])), ('clients', wagtail.blocks.StructBlock([('subtitle', base.blocks.basics.BaseCharBlock(help_text='Enter a subtitle for the clients section.', max_length=255, required=False)), ('logos', base.blocks.basics.BaseListBlock(wagtail.blocks.StructBlock([('image', base.blocks.basics.BaseImageBlock(help_text='Select a client logo image.', required=True)), ('alt_text', base.blocks.basics.BaseCharBlock(help_text='Enter an alternative text for the image.', max_length=255, required=False))]), help_text='Add client logos.'))]))], max_num=1))]))]))], blank=True, null=True),
        ),
    ]

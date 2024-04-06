# Generated by Django 5.0.2 on 2024-04-05 23:57

import base.blocks.basic
import base.blocks.lottie
import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_alter_homepage_hero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero',
            field=wagtail.fields.StreamField([('heading', base.blocks.basic.HeadingBlock()), ('paragraph', base.blocks.basic.ParagraphBlock()), ('button', wagtail.blocks.StructBlock([('page', wagtail.blocks.PageChooserBlock(required=True)), ('text', wagtail.blocks.CharBlock(required=False))])), ('lottie', wagtail.blocks.StructBlock([('lines', wagtail.blocks.StructBlock([('vertical', base.blocks.lottie.VerticalLines(help_text='Number of vertical lines.', required=False)), ('horizontal', base.blocks.lottie.HorizontalLines(help_text='Number of horizontal lines.', required=False))])), ('animation', base.blocks.lottie.LottieAnimation()), ('features', base.blocks.lottie.FeatureList())]))], blank=True, null=True),
        ),
    ]

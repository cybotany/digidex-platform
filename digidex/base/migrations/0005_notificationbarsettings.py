# Generated by Django 5.0.2 on 2024-04-02 01:30

import base.blocks
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_footersettings_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationBarSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notification', wagtail.fields.StreamField([('title', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock(form_classname='heading', required=True))])), ('icon', wagtail.blocks.StructBlock([('image', base.blocks.BaseImageBlock(help_text='Select an icon image', required=True)), ('item', wagtail.blocks.StructBlock([('text', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal', wagtail.blocks.PageChooserBlock(form_classname='heading', required=False)), ('external', wagtail.blocks.URLBlock(form_classname='heading', required=False))], required=False))]))]))], blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Notification Bar Settings',
            },
        ),
    ]

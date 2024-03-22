# Generated by Django 5.0.2 on 2024-03-22 04:15

import base.fields.django_fields
import base.fields.wagtail_fields
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='hero_cta',
            field=base.fields.django_fields.BaseCharField(blank=True, max_length=75, verbose_name='Hero CTA'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_cta_link',
            field=base.fields.django_fields.BaseForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Hero CTA link'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_heading',
            field=base.fields.django_fields.BaseCharField(blank=True, max_length=75),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='hero_text',
            field=base.fields.django_fields.BaseCharField(blank=True, max_length=150),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='lottie',
            field=base.fields.wagtail_fields.BaseRichTextField(blank=True),
        ),
    ]

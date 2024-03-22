# Generated by Django 5.0.2 on 2024-03-22 04:15

import base.models.django_fields
import base.models.wagtail_fields
import django.db.models.deletion
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='author_image',
            field=base.models.django_fields.BaseForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
        migrations.AlterField(
            model_name='author',
            name='name',
            field=base.models.django_fields.BaseCharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='blogindexpage',
            name='intro',
            field=base.models.wagtail_fields.BaseRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='body',
            field=base.models.wagtail_fields.BaseRichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='date',
            field=base.models.django_fields.BaseDateField(verbose_name='Post date'),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='intro',
            field=base.models.django_fields.BaseCharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='caption',
            field=base.models.django_fields.BaseCharField(blank=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='blogpagegalleryimage',
            name='image',
            field=base.models.django_fields.BaseForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image'),
        ),
    ]

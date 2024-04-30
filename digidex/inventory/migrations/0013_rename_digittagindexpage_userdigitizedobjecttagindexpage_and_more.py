# Generated by Django 5.0.2 on 2024-04-30 19:51

import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_userprofileindexpage_remove_user_avatar_and_more'),
        ('digitization', '0001_initial'),
        ('inventory', '0012_remove_digit_user_remove_digitpage_user_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DigitTagIndexPage',
            new_name='UserDigitizedObjectTagIndexPage',
        ),
        migrations.RemoveField(
            model_name='digit',
            name='user_page',
        ),
        migrations.RemoveField(
            model_name='digitpage',
            name='digit',
        ),
        migrations.RemoveField(
            model_name='digitformfield',
            name='page',
        ),
        migrations.RemoveField(
            model_name='digitpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='digitpage',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='digitpage',
            name='user_page',
        ),
        migrations.RemoveField(
            model_name='digitpagegalleryimage',
            name='page',
        ),
        migrations.RemoveField(
            model_name='digitpagegalleryimage',
            name='image',
        ),
        migrations.RemoveField(
            model_name='digitregistrationformpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='userindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='userpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='userpage',
            name='user',
        ),
        migrations.CreateModel(
            name='UserDigitizedObject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('digit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_associations', to='digitization.digitizedobject')),
                ('profile', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_digits', to='accounts.userprofilepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RenameModel(
            old_name='DigitPageTag',
            new_name='UserDigitizedObjectPageTag',
        ),
        migrations.CreateModel(
            name='UserDigitizedObjectPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('tags', modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='inventory.UserDigitizedObjectPageTag', to='taggit.Tag', verbose_name='Tags')),
                ('user_digit', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='digit_page', to='inventory.userdigitizedobject')),
                ('user_profile', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.PROTECT, related_name='digit_pages', to='accounts.userprofilepage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DigitizedObjectPageGalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='digitized_object_images', to='inventory.userdigitizedobjectpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='userdigitizedobjectpagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='inventory.userdigitizedobjectpage'),
        ),
    ]

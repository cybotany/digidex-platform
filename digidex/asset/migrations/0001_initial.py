# Generated by Django 5.0.2 on 2024-06-25 20:06

import django.db.models.deletion
import modelcluster.fields
import uuid
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('journal', '0001_initial'),
        ('nfc', '0001_initial'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssetNote',
            fields=[
                ('note_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.note')),
            ],
            options={
                'abstract': False,
            },
            bases=('journal.note',),
        ),
        migrations.CreateModel(
            name='AssetNoteImageGallery',
            fields=[
                ('noteimagegallery_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.noteimagegallery')),
                ('note', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='asset.assetnote')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=('journal.noteimagegallery',),
        ),
        migrations.CreateModel(
            name='AssetPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('description', wagtail.fields.RichTextField(blank=True, null=True)),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.collection')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='assetnote',
            name='asset',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='asset.assetpage'),
        ),
        migrations.CreateModel(
            name='AssetNearFieldCommunicationLink',
            fields=[
                ('nearfieldcommunicationlink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nfc.nearfieldcommunicationlink')),
                ('asset', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='asset.assetpage')),
            ],
            bases=('nfc.nearfieldcommunicationlink',),
        ),
    ]
# Generated by Django 5.0.2 on 2024-07-04 06:37

import django.db.models.deletion
import taggit.managers
import uuid
import wagtail.models.collections
import wagtail.search.index
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_inventorynote_options'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('entry', models.TextField(blank=True, verbose_name='entry')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'note',
                'verbose_name_plural': 'notes',
                'permissions': [('choose_document', 'Can choose document')],
                'abstract': False,
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.RemoveField(
            model_name='inventorynote',
            name='entry',
        ),
        migrations.AddField(
            model_name='inventory',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='expired'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='first_published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='go_live_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='go live date/time'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='has_unpublished_changes',
            field=models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='last_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='last published at'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='live',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='locale',
            field=models.ForeignKey(default=1, editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.locale'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='locked',
            field=models.BooleanField(default=False, editable=False, verbose_name='locked'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='locked_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='locked at'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='locked_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locked_%(class)ss', to=settings.AUTH_USER_MODEL, verbose_name='locked by'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='translation_key',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AddConstraint(
            model_name='inventory',
            constraint=models.UniqueConstraint(fields=('translation_key', 'locale'), name='unique_translation_key_locale'),
        ),
        migrations.AddField(
            model_name='note',
            name='collection',
            field=models.ForeignKey(default=wagtail.models.collections.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.collection', verbose_name='collection'),
        ),
        migrations.AddField(
            model_name='note',
            name='submitted_by_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='submitted by user'),
        ),
        migrations.AddField(
            model_name='note',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags'),
        ),
        migrations.AddField(
            model_name='inventorynote',
            name='body',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='inventory.note'),
        ),
    ]

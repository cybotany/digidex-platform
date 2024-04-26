# Generated by Django 5.0.2 on 2024-04-25 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_delete_footercopyright'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.AddField(
            model_name='footerinformation',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time'),
        ),
        migrations.AddField(
            model_name='footerinformation',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='expired'),
        ),
        migrations.AddField(
            model_name='footerinformation',
            name='first_published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at'),
        ),
        migrations.AddField(
            model_name='footerinformation',
            name='go_live_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='go live date/time'),
        ),
        migrations.AddField(
            model_name='footerinformation',
            name='has_unpublished_changes',
            field=models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes'),
        ),
        migrations.AddField(
            model_name='footerinformation',
            name='last_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='last published at'),
        ),
        migrations.AddField(
            model_name='footerinformation',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='footerinformation',
            name='live',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='footerinformation',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='expired'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='first_published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='go_live_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='go live date/time'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='has_unpublished_changes',
            field=models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='last_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='last published at'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='live',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='footerinternallinks',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='expire_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='expiry date/time'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='expired',
            field=models.BooleanField(default=False, editable=False, verbose_name='expired'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='first_published_at',
            field=models.DateTimeField(blank=True, db_index=True, null=True, verbose_name='first published at'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='go_live_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='go live date/time'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='has_unpublished_changes',
            field=models.BooleanField(default=False, editable=False, verbose_name='has unpublished changes'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='last_published_at',
            field=models.DateTimeField(editable=False, null=True, verbose_name='last published at'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='latest_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='latest revision'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='live',
            field=models.BooleanField(default=True, editable=False, verbose_name='live'),
        ),
        migrations.AddField(
            model_name='footersociallinks',
            name='live_revision',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.revision', verbose_name='live revision'),
        ),
    ]
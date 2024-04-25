# Generated by Django 5.0.2 on 2024-04-25 21:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_pagefooter_paragraph'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='FooterCopyright',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FooterInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paragraph', models.TextField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('chat', models.URLField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Primary Footer Information',
            },
        ),
        migrations.CreateModel(
            name='FooterSocialLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('github', models.URLField(blank=True, max_length=255, null=True, verbose_name='GitHub URL')),
                ('twitter', models.URLField(blank=True, max_length=255, null=True, verbose_name='Twitter URL')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='calltoactionbanner',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='calltoactionbanner',
            name='latest_revision',
        ),
        migrations.RemoveField(
            model_name='calltoactionbanner',
            name='live_revision',
        ),
        migrations.RemoveField(
            model_name='calltoactionbanner',
            name='locale',
        ),
        migrations.AlterUniqueTogether(
            name='navigationbar',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='navigationbar',
            name='latest_revision',
        ),
        migrations.RemoveField(
            model_name='navigationbar',
            name='live_revision',
        ),
        migrations.RemoveField(
            model_name='navigationbar',
            name='locale',
        ),
        migrations.RemoveField(
            model_name='pagefooter',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='pagefooter',
            name='company',
        ),
        migrations.RemoveField(
            model_name='pagefooter',
            name='solutions',
        ),
        migrations.RemoveField(
            model_name='pagefooter',
            name='support',
        ),
        migrations.RemoveField(
            model_name='sitesettings',
            name='logo',
        ),
        migrations.CreateModel(
            name='FooterInternalLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Blog Page')),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Company Page')),
                ('solutions', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Solutions Page')),
                ('support', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Support Page')),
            ],
        ),
        migrations.DeleteModel(
            name='AdvertBanner',
        ),
        migrations.DeleteModel(
            name='CallToActionBanner',
        ),
        migrations.DeleteModel(
            name='NavigationBar',
        ),
        migrations.DeleteModel(
            name='PageFooter',
        ),
        migrations.DeleteModel(
            name='SiteSettings',
        ),
    ]

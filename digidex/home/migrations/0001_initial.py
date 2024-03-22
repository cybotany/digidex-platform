# Generated by Django 5.0.2 on 2024-03-22 01:39

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('hero_heading', models.CharField(blank=True, max_length=75)),
                ('hero_text', models.CharField(blank=True, max_length=150)),
                ('hero_cta', models.CharField(blank=True, max_length=75, verbose_name='Hero CTA')),
                ('lottie', wagtail.fields.RichTextField(blank=True)),
                ('hero_cta_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page', verbose_name='Hero CTA link')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
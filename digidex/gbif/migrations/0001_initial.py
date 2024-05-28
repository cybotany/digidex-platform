# Generated by Django 5.0.2 on 2024-05-28 01:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset_id', models.CharField(max_length=255)),
                ('parent_name_usage_id', models.CharField(blank=True, max_length=255, null=True)),
                ('accepted_name_usage_id', models.CharField(blank=True, max_length=255, null=True)),
                ('original_name_usage_id', models.CharField(blank=True, max_length=255, null=True)),
                ('scientific_name', models.CharField(max_length=255)),
                ('scientific_name_authorship', models.CharField(blank=True, max_length=255, null=True)),
                ('canonical_name', models.CharField(blank=True, max_length=255, null=True)),
                ('generic_name', models.CharField(blank=True, max_length=255, null=True)),
                ('specific_epithet', models.CharField(blank=True, max_length=255, null=True)),
                ('infraspecific_epithet', models.CharField(blank=True, max_length=255, null=True)),
                ('taxon_rank', models.CharField(max_length=255)),
                ('name_according_to', models.CharField(blank=True, max_length=255, null=True)),
                ('name_published_in', models.CharField(blank=True, max_length=255, null=True)),
                ('taxonomic_status', models.CharField(max_length=255)),
                ('nomenclatural_status', models.CharField(blank=True, max_length=255, null=True)),
                ('taxon_remarks', models.TextField(blank=True, null=True)),
                ('kingdom', models.CharField(blank=True, max_length=255, null=True)),
                ('phylum', models.CharField(blank=True, max_length=255, null=True)),
                ('class_field', models.CharField(blank=True, max_length=255, null=True)),
                ('order', models.CharField(blank=True, max_length=255, null=True)),
                ('family', models.CharField(blank=True, max_length=255, null=True)),
                ('genus', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bibliographic_citation', models.TextField()),
                ('identifier', models.CharField(max_length=255)),
                ('references', models.TextField(blank=True, null=True)),
                ('source', models.CharField(max_length=255)),
                ('taxon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='references', to='gbif.taxon')),
            ],
        ),
        migrations.CreateModel(
            name='Multimedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=255)),
                ('references', models.TextField(blank=True, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('license', models.CharField(blank=True, max_length=255, null=True)),
                ('creator', models.CharField(blank=True, max_length=255, null=True)),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('contributor', models.CharField(blank=True, max_length=255, null=True)),
                ('publisher', models.CharField(blank=True, max_length=255, null=True)),
                ('rights_holder', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.CharField(blank=True, max_length=255, null=True)),
                ('taxon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='multimedia', to='gbif.taxon')),
            ],
        ),
        migrations.CreateModel(
            name='Distribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_id', models.CharField(max_length=255)),
                ('locality', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(max_length=255)),
                ('country_code', models.CharField(max_length=255)),
                ('location_remarks', models.TextField(blank=True, null=True)),
                ('establishment_means', models.CharField(blank=True, max_length=255, null=True)),
                ('life_stage', models.CharField(blank=True, max_length=255, null=True)),
                ('occurrence_status', models.CharField(max_length=255)),
                ('threat_status', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.CharField(max_length=255)),
                ('taxon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='distributions', to='gbif.taxon')),
            ],
        ),
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('source', models.CharField(max_length=255)),
                ('creator', models.CharField(blank=True, max_length=255, null=True)),
                ('contributor', models.CharField(blank=True, max_length=255, null=True)),
                ('license', models.CharField(blank=True, max_length=255, null=True)),
                ('taxon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='gbif.taxon')),
            ],
        ),
        migrations.CreateModel(
            name='TypesAndSpecimen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_designation_type', models.CharField(max_length=255)),
                ('type_designated_by', models.CharField(max_length=255)),
                ('scientific_name', models.CharField(max_length=255)),
                ('taxon_rank', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('taxon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='types_and_specimens', to='gbif.taxon')),
            ],
        ),
        migrations.CreateModel(
            name='VernacularName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vernacular_name', models.CharField(max_length=255)),
                ('language', models.CharField(max_length=255)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('country_code', models.CharField(blank=True, max_length=255, null=True)),
                ('sex', models.CharField(blank=True, max_length=255, null=True)),
                ('life_stage', models.CharField(blank=True, max_length=255, null=True)),
                ('source', models.CharField(max_length=255)),
                ('taxon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vernacular_names', to='gbif.taxon')),
            ],
        ),
    ]

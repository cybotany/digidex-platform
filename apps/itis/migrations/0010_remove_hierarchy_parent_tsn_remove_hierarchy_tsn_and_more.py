# Generated by Django 4.2.6 on 2023-10-30 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itis', '0009_delete_geographicdivision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hierarchy',
            name='parent_tsn',
        ),
        migrations.RemoveField(
            model_name='hierarchy',
            name='tsn',
        ),
        migrations.RemoveField(
            model_name='taxonomicunits',
            name='kingdom_id',
        ),
        migrations.RemoveField(
            model_name='taxonomicunits',
            name='parent_tsn',
        ),
        migrations.RemoveField(
            model_name='taxonomicunits',
            name='rank_id',
        ),
        migrations.RemoveField(
            model_name='taxonunittypes',
            name='kingdom_id',
        ),
        migrations.AddField(
            model_name='hierarchy',
            name='parent_taxonomic_unit',
            field=models.ForeignKey(blank=True, help_text='The direct parent TSN of hierarchy.TSN.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='child_taxonomic_units', to='itis.taxonomicunits', verbose_name='Parent TSN'),
        ),
        migrations.AddField(
            model_name='hierarchy',
            name='taxonomic_unit',
            field=models.ForeignKey(blank=True, help_text='The TSN for the hierarchy entry. The unique identifier for an occurrence of Taxonomic Units.', null=True, on_delete=django.db.models.deletion.CASCADE, to='itis.taxonomicunits', verbose_name='Taxonomic Serial Number'),
        ),
        migrations.AddField(
            model_name='taxonomicunits',
            name='kingdom',
            field=models.ForeignKey(blank=True, db_column='kingdom_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taxonomic_units', to='itis.kingdoms'),
        ),
        migrations.AddField(
            model_name='taxonomicunits',
            name='parent',
            field=models.ForeignKey(blank=True, db_column='parent_tsn', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='itis.taxonomicunits'),
        ),
        migrations.AddField(
            model_name='taxonomicunits',
            name='rank',
            field=models.ForeignKey(blank=True, db_column='rank_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='taxonomic_units', to='itis.taxonunittypes'),
        ),
        migrations.AddField(
            model_name='taxonunittypes',
            name='kingdom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itis.kingdoms', verbose_name='Kingdom'),
        ),
    ]

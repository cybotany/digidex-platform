# Generated by Django 4.2.9 on 2024-02-10 03:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('taxonomy', '0021_remove_unit_temp_g_remove_unit_temp_j'),
    ]

    operations = [
        migrations.RenameField(
            model_name='geography',
            old_name='geography',
            new_name='geography_value',
        ),
        migrations.RenameField(
            model_name='jurisdiction',
            old_name='jurisdiction',
            new_name='jurisdiction_value',
        ),
        migrations.RenameField(
            model_name='unitreferences',
            old_name='original_desc_ind',
            new_name='original_description_ind',
        ),
        migrations.RenameField(
            model_name='vernacular',
            old_name='language',
            new_name='vernacular_language',
        ),
        migrations.RemoveField(
            model_name='author',
            name='kingdom',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='initial_time_stamp',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='n_usage',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='phylo_sort_sequence',
        ),
        migrations.RemoveField(
            model_name='unitreferences',
            name='change_track_id',
        ),
        migrations.RemoveField(
            model_name='unitreferences',
            name='init_itis_desc_ind',
        ),
        migrations.RemoveField(
            model_name='unitreferences',
            name='vernacular_name',
        ),
        migrations.AddField(
            model_name='unit',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text='Date and time at which an occurrence of Taxonomic Units is initially loaded into the ITIS database.', verbose_name='Created At'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='geography',
            unique_together={('tsn', 'geography_value')},
        ),
        migrations.AlterUniqueTogether(
            name='jurisdiction',
            unique_together={('tsn', 'jurisdiction_value')},
        ),
        migrations.AlterUniqueTogether(
            name='vernacularreferences',
            unique_together={('vernacular', 'content_type', 'object_id')},
        ),
        migrations.RemoveField(
            model_name='vernacularreferences',
            name='tsn',
        ),
    ]

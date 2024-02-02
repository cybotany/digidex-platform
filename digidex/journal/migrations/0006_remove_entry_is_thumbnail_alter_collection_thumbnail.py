# Generated by Django 4.2.6 on 2024-02-02 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0005_alter_collection_thumbnail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='is_thumbnail',
        ),
        migrations.AlterField(
            model_name='collection',
            name='thumbnail',
            field=models.ForeignKey(blank=True, help_text='Reference to the entry that contains the thumbnail image.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='journal_thumbnail', to='journal.entry'),
        ),
    ]

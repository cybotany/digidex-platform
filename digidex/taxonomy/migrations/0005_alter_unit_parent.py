# Generated by Django 4.2.9 on 2024-02-09 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0004_alter_unit_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='parent',
            field=models.SmallIntegerField(blank=True, help_text='The taxonomic serial number for the direct parent of the subject occurrence of Taxonomic Units.', null=True, verbose_name='Parent TSN'),
        ),
    ]

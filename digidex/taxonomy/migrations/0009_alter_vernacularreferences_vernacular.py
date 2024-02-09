# Generated by Django 4.2.9 on 2024-02-09 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0008_rename_jurisdiction_value_jurisdiction_jurisdiction_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vernacularreferences',
            name='vernacular',
            field=models.IntegerField(db_column='vernacular_id', help_text='Unique identifier for the vernacular name entry.'),
        ),
    ]

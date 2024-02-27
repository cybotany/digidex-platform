# Generated by Django 4.2.9 on 2024-02-27 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_grouping_slug_pet_digit_type_plant_digit_type_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='grouping',
            name='is_default',
            field=models.BooleanField(default=False, help_text='Indicates if this is the default grouping for the user. Default groupings cannot be deleted.'),
        ),
    ]

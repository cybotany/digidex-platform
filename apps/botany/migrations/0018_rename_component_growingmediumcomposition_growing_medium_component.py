# Generated by Django 4.1.7 on 2023-07-03 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('botany', '0017_growingmediumcomponent_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='growingmediumcomposition',
            old_name='component',
            new_name='growing_medium_component',
        ),
    ]

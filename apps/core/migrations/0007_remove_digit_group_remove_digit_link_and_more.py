# Generated by Django 4.2.6 on 2023-12-09 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_digit_taxonomic_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digit',
            name='group',
        ),
        migrations.RemoveField(
            model_name='digit',
            name='link',
        ),
        migrations.RemoveField(
            model_name='digit',
            name='user',
        ),
    ]

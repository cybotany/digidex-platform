# Generated by Django 5.0.2 on 2024-04-29 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0008_digittagindexpage_alter_digit_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='digit',
            old_name='page',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='digit',
            name='ntag',
        ),
    ]
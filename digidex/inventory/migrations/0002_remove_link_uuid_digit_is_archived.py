# Generated by Django 4.2.6 on 2024-01-28 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='uuid',
        ),
        migrations.AddField(
            model_name='digit',
            name='is_archived',
            field=models.BooleanField(default=False, help_text='Indicates whether the digit is archived.', verbose_name='Archived'),
        ),
    ]

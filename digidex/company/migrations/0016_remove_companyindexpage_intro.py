# Generated by Django 5.0.6 on 2024-08-03 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0015_remove_teammemberrole_sort_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companyindexpage',
            name='intro',
        ),
    ]
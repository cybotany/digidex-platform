# Generated by Django 5.0.2 on 2024-04-01 03:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_accountindexpage'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccountPage',
        ),
    ]
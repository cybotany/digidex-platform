# Generated by Django 5.0.2 on 2024-05-31 16:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='category',
            name='profile',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='inventory_categories', to='inventory.userprofile'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='category',
            name='user',
        ),
    ]

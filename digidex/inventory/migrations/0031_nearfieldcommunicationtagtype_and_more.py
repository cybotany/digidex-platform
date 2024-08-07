# Generated by Django 5.0.6 on 2024-08-08 22:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0030_nearfieldcommunicationtag_label'),
    ]

    operations = [
        migrations.CreateModel(
            name='NearFieldCommunicationTagType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('form', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'verbose_name': 'near field communication tag type',
                'verbose_name_plural': 'near field communication tag types',
            },
        ),
        migrations.RemoveField(
            model_name='nearfieldcommunicationtag',
            name='form',
        ),
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='inventory.nearfieldcommunicationtagtype'),
        ),
    ]

# Generated by Django 5.0.6 on 2024-07-28 04:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('inventorytags', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nearfieldcommunicationtag',
            name='link',
        ),
        migrations.CreateModel(
            name='InventoryLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField(blank=True, db_index=True, null=True)),
                ('link', models.URLField(blank=True, max_length=255, null=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('tag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='inventorytags.nearfieldcommunicationtag')),
            ],
            options={
                'verbose_name': 'inventory link',
                'verbose_name_plural': 'inventory links',
                'indexes': [models.Index(fields=['content_type'], name='inventoryta_content_049509_idx'), models.Index(fields=['object_id'], name='inventoryta_object__9f38cf_idx'), models.Index(fields=['tag'], name='inventoryta_tag_id_c71626_idx')],
            },
        ),
    ]
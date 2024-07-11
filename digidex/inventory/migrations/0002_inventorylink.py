# Generated by Django 5.0.6 on 2024-07-11 22:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
        ('nearfieldcommunication', '0001_initial'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryLink',
            fields=[
                ('nearfieldcommunicationtag_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='nearfieldcommunication.nearfieldcommunicationtag')),
                ('resource', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'links',
            },
            bases=('nearfieldcommunication.nearfieldcommunicationtag',),
        ),
    ]
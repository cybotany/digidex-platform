# Generated by Django 5.0.6 on 2024-07-22 03:25

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_delete_inventorypage'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('body', models.TextField(blank=True, null=True, verbose_name='body')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('inventory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='file', to='inventory.userinventory', verbose_name='inventory')),
            ],
            options={
                'verbose_name': 'inventory asset',
                'verbose_name_plural': 'inventory assets',
            },
        ),
        migrations.DeleteModel(
            name='InventoryAsset',
        ),
    ]
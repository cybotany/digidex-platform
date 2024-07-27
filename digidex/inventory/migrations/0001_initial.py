# Generated by Django 5.0.6 on 2024-07-27 19:27

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0093_uploadedfile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.collection')),
                ('owner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'user inventory',
                'verbose_name_plural': 'user inventories',
            },
        ),
        migrations.CreateModel(
            name='InventoryCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.collection')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='inventory.userinventory', verbose_name='inventory')),
            ],
            options={
                'verbose_name': 'inventory category',
                'verbose_name_plural': 'inventory categories',
            },
        ),
        migrations.CreateModel(
            name='InventoryAsset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.collection')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='inventory.inventorycategory', verbose_name='category')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assets', to='inventory.userinventory', verbose_name='inventory')),
            ],
            options={
                'verbose_name': 'inventory asset',
                'verbose_name_plural': 'inventory assets',
            },
        ),
        migrations.AddConstraint(
            model_name='userinventory',
            constraint=models.UniqueConstraint(fields=('slug',), name='unique_user_inventory_slug'),
        ),
        migrations.AddConstraint(
            model_name='inventorycategory',
            constraint=models.UniqueConstraint(fields=('inventory', 'slug'), name='unique_inventory_category_slug'),
        ),
        migrations.AddConstraint(
            model_name='inventoryasset',
            constraint=models.UniqueConstraint(fields=('inventory', 'category', 'slug'), name='unique_inventory_asset_slug'),
        ),
    ]

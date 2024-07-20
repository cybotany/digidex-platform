# Generated by Django 5.0.6 on 2024-07-20 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InventoryLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='inventory.inventory')),
                ('tag', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='link', to='inventory.inventorytag')),
            ],
        ),
    ]

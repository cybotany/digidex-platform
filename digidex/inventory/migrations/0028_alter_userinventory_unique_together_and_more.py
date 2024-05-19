# Generated by Django 5.0.2 on 2024-05-19 00:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0027_alter_userdigit_page'),
        ('profiles', '0003_alter_userprofile_bio'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userinventory',
            unique_together={('profile_page', 'name')},
        ),
        migrations.AddField(
            model_name='userinventory',
            name='description',
            field=models.TextField(blank=True, help_text='Digitized object Inventory description.', null=True),
        ),
        migrations.AlterField(
            model_name='userinventory',
            name='detail_page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='detailed_digit', to='inventory.userinventorypage'),
        ),
    ]

# Generated by Django 4.2.9 on 2024-02-22 22:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_rename_taxonomic_unit_digit_taxon_and_more'),
        ('link', '0004_ntag_delete_nfc'),
    ]

    operations = [
        migrations.AddField(
            model_name='digit',
            name='ntag',
            field=models.OneToOneField(blank=True, help_text='NTAG link for the digitized plant.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='digit', to='link.ntag'),
        ),
        migrations.AlterField(
            model_name='digit',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, help_text='The unique identifier associated with the Digit.', unique=True, verbose_name='Digit UUID'),
        ),
    ]

# Generated by Django 4.2.6 on 2024-01-31 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0002_remove_nfc_uuid'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='digit',
            name='nfc_link',
            field=models.OneToOneField(blank=True, help_text='NFC link for the digitized plant.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='digit', to='link.nfc'),
        ),
    ]

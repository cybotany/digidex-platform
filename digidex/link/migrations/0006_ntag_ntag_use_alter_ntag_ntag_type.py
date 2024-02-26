# Generated by Django 4.2.9 on 2024-02-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0005_remove_ntag_manufacturer_remove_ntag_version_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ntag',
            name='ntag_use',
            field=models.CharField(choices=[('plant_label', 'Plant Label'), ('pet_tag', 'Pet Tag')], default='plant_label', help_text='The intended use of the NTAG.', max_length=20, verbose_name='NTAG Use'),
        ),
        migrations.AlterField(
            model_name='ntag',
            name='ntag_type',
            field=models.CharField(blank=True, choices=[('NTAG_424_DNA_TagTamper', 'NTAG 424 DNA TagTamper'), ('NTAG_424_DNA', 'NTAG 424 DNA'), ('NTAG_426Q_DNA', 'NTAG 426Q DNA'), ('NTAG_223_DNA', 'NTAG 223 DNA'), ('NTAG_224_DNA', 'NTAG 224 DNA'), ('NTAG_223_DNA_StatusDetect', 'NTAG 223 DNA StatusDetect'), ('NTAG_224_DNA_StatusDetect', 'NTAG 224 DNA StatusDetect'), ('NTAG_213_TagTamper', 'NTAG 213 TagTamper'), ('NTAG_213', 'NTAG 213'), ('NTAG_215', 'NTAG 215'), ('NTAG_216', 'NTAG 216'), ('NTAG_210', 'NTAG 210'), ('NTAG_212', 'NTAG 212')], default='NTAG_213', help_text='The type of the NTAG.', max_length=25, verbose_name='NTAG Type'),
        ),
    ]

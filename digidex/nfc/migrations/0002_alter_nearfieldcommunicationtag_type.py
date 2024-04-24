# Generated by Django 5.0.2 on 2024-04-24 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nfc', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearfieldcommunicationtag',
            name='type',
            field=models.CharField(blank=True, choices=[('ntag_213', 'NTAG 213'), ('ntag_215', 'NTAG 215'), ('ntag_216', 'NTAG 216')], default='NTAG_213', help_text='The type of the NTAG.', max_length=25, verbose_name='NTAG Type'),
        ),
    ]
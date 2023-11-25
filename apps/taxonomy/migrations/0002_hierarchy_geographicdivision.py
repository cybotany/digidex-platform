# Generated by Django 4.2.6 on 2023-11-25 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taxonomy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hierarchy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geographic_value', models.CharField(blank=True, max_length=200, null=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('tsn', models.ForeignKey(blank=True, db_column='tsn', null=True, on_delete=django.db.models.deletion.CASCADE, to='taxonomy.units', verbose_name='Taxonomic Serial Number')),
            ],
        ),
        migrations.CreateModel(
            name='GeographicDivision',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('geographic_value', models.CharField(blank=True, max_length=200, null=True)),
                ('update_date', models.DateTimeField(auto_now_add=True)),
                ('tsn', models.ForeignKey(blank=True, db_column='tsn', null=True, on_delete=django.db.models.deletion.CASCADE, to='taxonomy.units', verbose_name='Taxonomic Serial Number')),
            ],
        ),
    ]

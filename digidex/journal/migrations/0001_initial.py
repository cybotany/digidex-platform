# Generated by Django 5.0.2 on 2024-05-20 01:20

import django.db.models.deletion
import modelcluster.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('digitization', '0008_initial'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('caption', models.CharField(blank=True, help_text='Image caption.', max_length=250, null=True)),
                ('digit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='journal_entries', to='digitization.userdigit')),
                ('image', models.ForeignKey(help_text='Digitized object image.', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.image')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='digit_journal_entries', to='digitization.userdigitpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]

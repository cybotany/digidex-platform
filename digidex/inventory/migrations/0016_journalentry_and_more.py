# Generated by Django 5.0.6 on 2024-08-06 21:41

import django.db.models.deletion
import modelcluster.fields
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0015_alter_assetjournalentry_note'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AssetJournalEntry',
            new_name='JournalEntry',
        ),
        migrations.AlterField(
            model_name='journalgallerydocument',
            name='journal_entry',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_documents', to='inventory.journalentry'),
        ),
        migrations.AlterField(
            model_name='journalgalleryimage',
            name='journal_entry',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery_images', to='inventory.journalentry'),
        ),
    ]
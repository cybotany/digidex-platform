# Generated by Django 5.0.2 on 2024-06-27 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_delete_inventorynearfieldcommunicationlink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorynoteimagegallery',
            name='note',
        ),
        migrations.RemoveField(
            model_name='inventorynoteimagegallery',
            name='noteimagegallery_ptr',
        ),
        migrations.DeleteModel(
            name='InventoryNote',
        ),
        migrations.DeleteModel(
            name='InventoryNoteImageGallery',
        ),
    ]

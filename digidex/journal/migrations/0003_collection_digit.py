# Generated by Django 4.2.9 on 2024-02-11 03:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_remove_digit_journal_collection_and_more'),
        ('journal', '0002_alter_entry_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='digit',
            field=models.OneToOneField(default=1, help_text='The digit associated with this journal collection.', on_delete=django.db.models.deletion.CASCADE, related_name='journal_collection', to='inventory.digit'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.2 on 2024-06-27 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0003_alter_trainernote_options_alter_trainerpage_options_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrainerNearFieldCommunicationLink',
        ),
    ]
# Generated by Django 5.0.2 on 2024-03-25 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0004_remove_supportindexpage_call_to_action_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supportpage',
            name='page_ptr',
        ),
        migrations.DeleteModel(
            name='SupportIndexPage',
        ),
        migrations.DeleteModel(
            name='SupportPage',
        ),
    ]
# Generated by Django 5.0.2 on 2024-05-10 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digitization', '0005_alter_digitizedobject_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='digitizedobjectimage',
            name='digit',
        ),
        migrations.RemoveField(
            model_name='digitizedobjectimage',
            name='image',
        ),
    ]

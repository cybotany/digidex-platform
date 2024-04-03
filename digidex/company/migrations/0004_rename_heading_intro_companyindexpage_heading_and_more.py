# Generated by Django 5.0.2 on 2024-04-02 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_companyindexpage_lottie_animation_1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companyindexpage',
            old_name='heading_intro',
            new_name='heading',
        ),
        migrations.RemoveField(
            model_name='companyindexpage',
            name='heading_title',
        ),
        migrations.AddField(
            model_name='companyindexpage',
            name='intro',
            field=models.TextField(blank=True, null=True),
        ),
    ]
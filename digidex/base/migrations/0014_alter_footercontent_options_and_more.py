# Generated by Django 5.0.2 on 2024-04-02 23:41

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_alter_footercontent_options'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='footercontent',
            options={'verbose_name_plural': 'Footer Content'},
        ),
        migrations.RenameField(
            model_name='footercontent',
            old_name='body',
            new_name='paragraph',
        ),
        migrations.RemoveField(
            model_name='footercontent',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='footernotice',
            name='copyright',
        ),
        migrations.RemoveField(
            model_name='footernotice',
            name='credit',
        ),
        migrations.AddField(
            model_name='footernotice',
            name='notice',
            field=wagtail.fields.RichTextField(blank=True, help_text='Copyright and Credit notices for the footer.'),
        ),
        migrations.AddField(
            model_name='navigationsettings',
            name='logo',
            field=models.ForeignKey(blank=True, help_text='Company Logo.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image'),
        ),
    ]
# Generated by Django 5.0.2 on 2024-04-30 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_rename_digittagindexpage_userdigitizedobjecttagindexpage_and_more'),
        ('nfc', '0010_alter_nearfieldcommunicationtag_digit'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Digit',
        ),
        migrations.DeleteModel(
            name='DigitFormField',
        ),
        migrations.DeleteModel(
            name='DigitPage',
        ),
        migrations.DeleteModel(
            name='DigitPageGalleryImage',
        ),
        migrations.DeleteModel(
            name='DigitRegistrationFormPage',
        ),
        migrations.DeleteModel(
            name='UserIndexPage',
        ),
        migrations.DeleteModel(
            name='UserPage',
        ),
    ]

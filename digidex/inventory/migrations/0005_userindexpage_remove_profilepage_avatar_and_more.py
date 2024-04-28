# Generated by Django 5.0.2 on 2024-04-28 22:17

import django.db.models.deletion
import uuid
import wagtail.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_rename_userprofilepage_profilepage'),
        ('nfc', '0003_remove_nearfieldcommunicationtag_counter_and_more'),
        ('wagtailcore', '0091_remove_revision_submitted_for_moderation'),
        ('wagtailimages', '0025_alter_image_file_alter_rendition_file'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='profilepage',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='profilepage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='profilepage',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userdigit',
            name='ntag',
        ),
        migrations.CreateModel(
            name='Digit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='Digit UUID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('ntag', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='digit', to='nfc.nearfieldcommunicationtag')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='UserPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('biography', wagtail.fields.RichTextField(blank=True, null=True)),
                ('avatar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_pages', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Page',
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='DigitPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('description', wagtail.fields.RichTextField(blank=True)),
                ('digit', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='pages', to='inventory.digit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='digits', to='inventory.userpage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='ProfileIndexPage',
        ),
        migrations.DeleteModel(
            name='ProfilePage',
        ),
        migrations.DeleteModel(
            name='UserDigit',
        ),
    ]
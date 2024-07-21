# Generated by Django 5.0.6 on 2024-07-21 20:28

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_homepage_options'),
        ('wagtailcore', '0093_uploadedfile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={'verbose_name': 'home page'},
        ),
        migrations.CreateModel(
            name='AdminPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.fields.RichTextField(blank=True, null=True, verbose_name='body')),
                ('collection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.collection')),
            ],
            options={
                'verbose_name': 'home page',
            },
            bases=('wagtailcore.page',),
        ),
    ]

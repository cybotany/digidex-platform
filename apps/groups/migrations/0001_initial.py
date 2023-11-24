# Generated by Django 4.2.6 on 2023-11-23 22:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the group.', max_length=50)),
                ('position', models.PositiveIntegerField(help_text='The position/order of the group.')),
                ('user', models.ForeignKey(blank=True, help_text='The user who created the group.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'group',
                'verbose_name_plural': 'groups',
                'ordering': ['position'],
                'unique_together': {('name', 'user'), ('position', 'user')},
            },
        ),
    ]

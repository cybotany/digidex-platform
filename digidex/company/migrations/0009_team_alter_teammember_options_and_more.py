# Generated by Django 5.0.6 on 2024-08-03 21:49

import django.db.models.deletion
import modelcluster.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0008_alter_teammember_role'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'company team',
                'verbose_name_plural': 'company teams',
            },
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'verbose_name': 'team member', 'verbose_name_plural': 'team members'},
        ),
        migrations.AlterModelOptions(
            name='teammemberrole',
            options={'verbose_name': 'member role', 'verbose_name_plural': 'member roles'},
        ),
        migrations.RemoveField(
            model_name='companyindexpage',
            name='team_members',
        ),
        migrations.RemoveField(
            model_name='teammemberrole',
            name='role_title',
        ),
        migrations.AddField(
            model_name='teammember',
            name='sort_order',
            field=models.IntegerField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='teammemberrole',
            name='name',
            field=models.CharField(default='Founder', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='companyindexpage',
            name='intro',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_members', to='company.teammemberrole'),
        ),
        migrations.AlterField(
            model_name='teammember',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='companyindexpage',
            name='team',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='company.team'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='team',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='members', to='company.team'),
        ),
    ]

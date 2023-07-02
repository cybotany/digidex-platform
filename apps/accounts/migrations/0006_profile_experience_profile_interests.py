# Generated by Django 4.1.7 on 2023-07-02 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_activity'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='experience',
            field=models.CharField(blank=True, choices=[('beginner', 'Beginner'), ('intermediate', 'Intermediate'), ('advanced', 'Advanced'), ('expert', 'Expert')], help_text='Experience of the user.', max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='interests',
            field=models.CharField(blank=True, choices=[('gardening', 'Gardening'), ('hydroponics', 'Hydroponics'), ('botany', 'Botany'), ('farming', 'Farming')], help_text='Interests of the user.', max_length=100),
        ),
    ]

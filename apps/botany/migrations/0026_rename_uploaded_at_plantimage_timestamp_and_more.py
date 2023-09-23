# Generated by Django 4.1.7 on 2023-09-23 02:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('botany', '0025_remove_plant_is_active_remove_plant_label_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plantimage',
            old_name='uploaded_at',
            new_name='timestamp',
        ),
        migrations.CreateModel(
            name='PlantWatering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watered', models.BooleanField(default=False, help_text='Whether the plant was watered.')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now, help_text='The date and time when the plant was watered.')),
                ('plant', models.ForeignKey(help_text='The plant associated with this watering event.', on_delete=django.db.models.deletion.CASCADE, related_name='waterings', to='botany.plant')),
            ],
        ),
    ]

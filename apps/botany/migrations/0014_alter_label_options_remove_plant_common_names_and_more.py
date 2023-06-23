# Generated by Django 4.1.7 on 2023-06-23 21:31

import apps.utils.custom_storage
import apps.utils.helpers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('botany', '0013_remove_plant_edible_parts_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='label',
            options={'verbose_name': 'label', 'verbose_name_plural': 'labels'},
        ),
        migrations.RemoveField(
            model_name='plant',
            name='common_names',
        ),
        migrations.AlterField(
            model_name='label',
            name='is_common',
            field=models.BooleanField(default=False, help_text='Is this a common label.'),
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(help_text='The name of the label.', max_length=50),
        ),
        migrations.AlterField(
            model_name='label',
            name='user',
            field=models.ForeignKey(blank=True, help_text='The user who created the label. Null for common labels.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='plantimage',
            name='image',
            field=models.ImageField(help_text='The image file. Only .jpg, .png, and .jpeg extensions are allowed.', upload_to=apps.utils.custom_storage.PlantImageStorage(apps.utils.helpers.user_directory_path), validators=[apps.utils.helpers.validate_file_extension]),
        ),
        migrations.AlterField(
            model_name='plantimage',
            name='plant',
            field=models.ForeignKey(help_text='The plant associated with this image.', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='botany.plant'),
        ),
        migrations.AlterField(
            model_name='plantimage',
            name='uploaded_at',
            field=models.DateTimeField(auto_now_add=True, help_text='The date and time when the image was uploaded.'),
        ),
    ]

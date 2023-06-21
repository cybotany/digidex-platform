from django.db import models
from django.contrib.auth import get_user_model
from apps.botany.models import Plant
from apps.utils.helpers import user_directory_path, validate_file_extension

User = get_user_model()


class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=user_directory_path, validators=[validate_file_extension])

    def __str__(self):
        return f'Image for {self.plant.name}'

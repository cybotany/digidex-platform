from django.db import models
from django.contrib.auth import get_user_model
from apps.utils.helpers import user_directory_path, validate_file_extension
from apps.utils.custom_storage import PlantImageStorage
from .plant import Plant

User = get_user_model()


class PlantImage(models.Model):
    plant = models.ForeignKey(Plant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=PlantImageStorage(user_directory_path), validators=[validate_file_extension])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Image for {self.plant.name}'


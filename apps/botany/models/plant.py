import os
import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .label import Label

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.png', '.jpeg']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def user_directory_path(instance, filename):
    # get the file extension
    ext = filename.split('.')[-1]
    # generate a UUID for the new filename
    filename = f'{uuid.uuid4()}.{ext}'
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return os.path.join(f'owner_{instance.owner.id}', filename)

User = get_user_model()


class Plant(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    label = models.ForeignKey(Label, on_delete=models.SET_NULL, null=True)
    common_names = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    edible_parts = models.TextField(null=True, blank=True)
    gbif_species_id = models.CharField(max_length=200, null=True, blank=True)
    propagation_methods = models.TextField(null=True, blank=True)
    scientific_name = models.CharField(max_length=200, null=True, blank=True)
    synonyms = models.TextField(null=True, blank=True)
    taxonomy = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=user_directory_path, validators=[validate_file_extension], null=True, blank=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.name:
            total_plants = Plant.objects.filter(owner=self.owner).count()
            self.name = f'Plant-{total_plants + 1}'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

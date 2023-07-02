from django.db import models
from apps.utils.helpers import user_directory_path
from apps.utils.custom_storage import PlantImageStorage

from .plant import Plant


class PlantImage(models.Model):
    """
    Represents an image of a plant.

    Attributes:
        plant (ForeignKey): The plant associated with this image.
        image (ImageField): The image file.
        uploaded_at (DateTimeField): The date and time when the image was uploaded.
    """

    plant = models.ForeignKey(
        Plant,
        related_name='images',
        on_delete=models.CASCADE,
        help_text="The plant associated with this image."
    )

    image = models.ImageField(
        upload_to=PlantImageStorage(user_directory_path),
        help_text="The image file. Only .jpg, .png, and .jpeg extensions are allowed."
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time when the image was uploaded."
    )

    def __str__(self):
        """
        Returns a string representation of the image,
        indicating which plant it is associated with.

        Returns:
            str: A string representation of the plant image.
        """
        return f'Image for {self.plant.name}'

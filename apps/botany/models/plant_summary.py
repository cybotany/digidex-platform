from django.db import models
from apps.nfc.models import Tag
from apps.botany.models import Plant, PlantImage, PlantWatering, PlantFertilization

class PlantCard(models.Model):
    """
    Represents a consolidated document for a plant, suitable for use in RAG.

    Attributes:
        tag (OneToOneField): The NFC Tag ID, which also acts as the ID for this document.
        title (CharField): A short title or name for the plant.
        description (TextField): A detailed description of the plant.
        images (ManyToManyField): Associated images of the plant.
        watering_events (ManyToManyField): Associated watering events.
        fertilization_events (ManyToManyField): Associated fertilization events.
    """

    tag = models.OneToOneField(
        Tag,
        primary_key=True,
        on_delete=models.CASCADE,
        related_name='plant_card'
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    images = models.ManyToManyField(PlantImage)
    watering_events = models.ManyToManyField(PlantWatering)
    fertilization_events = models.ManyToManyField(PlantFertilization)

    def __str__(self):
        return self.title

    def generate_description(self):
        """
        Generate a detailed description based on associated data.
        This can be used to populate the 'description' field.
        """
        description_parts = [
            f"Plant Name: {self.title}",
            f"Description: {self.description}",
            f"Number of Images: {self.images.count()}",
            f"Number of Watering Events: {self.watering_events.count()}",
            f"Number of Fertilization Events: {self.fertilization_events.count()}",
        ]
        return "\n".join(description_parts)

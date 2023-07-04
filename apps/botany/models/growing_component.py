from django.db import models
from apps.utils.constants import GROWING_MEDIUM_COMPONENT, MEASUREMENT_CHOICES


class GrowingComponent(models.Model):
    """
    Represents a single type of growing medium component.

    Fields:
        component (CharField): A char field for growing medium component, maximum length 100 characters.
        description (TextField): A text field used for describing the growing medium component.
        particle_size (DecimalField): A decimal field for specifying the particle size of the growing medium component.
        particle_size_unit (CharField): A char field for specifying the unit of measurement for the particle size.
    """
    component = models.CharField(
        max_length=100,
        choices=GROWING_MEDIUM_COMPONENT,
        blank=False,
        null=False,
        help_text='Components used as growing medium for plants.'
    )
    description = models.TextField(
        blank=True,
        null=False,
        help_text='Description for plant growing medium components.'
    )
    particle_size = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        blank=True,
        null=True,
        help_text='Particle size of the growing medium component.'
    )
    particle_size_unit = models.CharField(
        max_length=50,
        choices=MEASUREMENT_CHOICES,
        blank=True,
        null=True,
        help_text='Unit of measurement for the particle size.'
    )

    def __str__(self):
        return self.component

from django.db import models
from django.contrib.auth import get_user_model


class Fertilizer(models.Model):
    """
    Represents a fertilizer with nutrient composition.

    Fields:
        user (ForeignKey): Reference to the user who added this fertilizer.
        name (CharField): The brand name of the fertilizer.
        description (TextField): A description of the fertilizer.
        nitrogen (DecimalField): The percentage of nitrogen content.
        phosphorus (DecimalField): The percentage of phosphorus content.
        potassium (DecimalField): The percentage of potassium content.
        added_on (DateTimeField): The date and time when the fertilizer was added.
    """

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        help_text='Brand name of the fertilizer.'
    )
    description = models.TextField(
        blank=True,
        help_text='Description of the fertilizer.'
    )
    nitrogen = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='Percentage of nitrogen content in the fertilizer.'
    )
    phosphorus = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='Percentage of phosphorus content in the fertilizer.'
    )
    potassium = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='Percentage of potassium content in the fertilizer.'
    )
    added_on = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.name} (N:{self.nitrogen}% P:{self.phosphorus}% K:{self.potassium}%)"

    class Meta:
        ordering = ['-added_on']

from django.db import models
from digidex.inventory.models.digit.animal.pet import base

class PetDog(base.Pet):
    """
    A dog that is a pet.
    
    Attributes:
    - size: The size of the dog.
    
    Methods:
    - get_kingdom_id: Return the kingdom ID for animals.
    """
    DOG_SIZES = (
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
    )
    size = models.CharField(
        max_length=50,
        choices=DOG_SIZES,
        default='medium',
    )

    def get_kingdom_id(self):
        """
        Return the kingdom ID for animals.
        """
        return 5

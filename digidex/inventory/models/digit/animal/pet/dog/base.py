from django.db import models

from digidex.inventory.models.digit.animal.pet import base as base_pet

class PetDog(base_pet.Pet):
    """
    A digitized representation of a pet dog.
    
    Attributes:
    - size: The size of the dog.
    
    Methods:
    - get_taxon: Return the Taxonimic Serial Number ID for domesticated dogs.
    """
    _itis_taxon_pk = 726821
    _itis_rank_pk = 123

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

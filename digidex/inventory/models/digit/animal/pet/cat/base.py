from django.db import models

from digidex.inventory.models.digit.animal.pet import base as base_pet

class PetCat(base_pet.Pet):
    """
    A digitized representation of a pet cat.
    
    Attributes:
    - indoor (BooleanField): The size of the dog.
    
    Methods:
    - get_taxon: Return the Taxonimic Serial Number ID for domesticated dogs.
    """
    _taxon_pk = 183798

    indoor = models.BooleanField(
        default=True,
        help_text="Indicates whether the cat is an indoor cat or not."
    )

    def get_kingdom_id(self):
        """
        Return the kingdom ID for animals.
        """
        return 5

from django.db import models

from digidex.inventory.models.digit.animal.pet import base as base_pet

class PetCat(base_pet.Pet):
    """
    A digitized representation of a pet cat.
    
    Attributes:
    - indoor (BooleanField): Indicates whether the cat is an indoor cat or not.
    
    Methods:
    - get_taxon: Return the Taxonimic Serial Number ID for domesticated cats.
    """
    _taxon_pk = 183798
    _rank_pk = 122

    indoor = models.BooleanField(
        default=True,
        help_text="Indicates whether the cat is an indoor cat or not."
    )

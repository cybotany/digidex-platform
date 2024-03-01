from django.db import models
from django.core.exceptions import ObjectDoesNotExist


from digidex.taxonomy.models.taxon import base as base_taxon
from digidex.inventory.models.digit.animal.pet import base as base_pet

class PetDog(base_pet.Pet):
    """
    A digitized representation of a pet dog.
    
    Attributes:
    - size: The size of the dog.
    
    Methods:
    - get_taxon: Return the Taxonimic Serial Number ID for domesticated dogs.
    """
    _taxon_pk = 726821

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

    @classmethod
    def get_taxon(cls):
        try:
            return base_taxon.Taxon.objects.get(pk=cls._taxon_pk)
        except ObjectDoesNotExist:
            raise ValueError(f"Taxon with the specified serial number {cls._taxon_pk} does not exist.")

    def save(self, *args, **kwargs):
        if not self.taxon:
            self.taxon = self.get_taxon()
        super().save(*args, **kwargs)

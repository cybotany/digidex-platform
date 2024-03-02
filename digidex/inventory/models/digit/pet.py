from django.db import models
from digidex.inventory.models.digit import _base

class _DigitizedAnimal(_base._Digit):
    """
    A digitized representation of an animal.
    """
    _itis_kingdom_pk = 5
    _itis_rank_pk = 98
    _itis_taxon_pk = 202423
    
    class Meta:
        abstract = True

class _DigitizedPet(_DigitizedAnimal):
    """
    A class representing a pet digit.

    Attributes:
    - age (PositiveIntegerField): The age of the pet in years.
    - breed (CharField): The pet breed.
    - records (JSONField): A list of records for the pet.
    """
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="The age of the pet in years."
    )
    breed = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="The pet breed."
    )
    records = models.JSONField(
        default=list,
        blank=True,
        null=True,
        help_text="A list of records for the pet."
    )

    class Meta:
        abstract = True

class DigitizedPetCat(_DigitizedPet):
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

class DigitizedPetDog(_DigitizedPet):
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

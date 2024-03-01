from django.core.exceptions import ObjectDoesNotExist

from digidex.inventory.models.digit import base as base_digit
from digidex.taxonomy.models import kingdom as taxon_kingdom

class Animal(base_digit.Digit):
    """
    A digitized representation of a pet dog.
    
    """
    _kingdom_id = 5

    @classmethod
    def get_kingdom(cls):
        try:
            return taxon_kingdom.Kingdom.objects.get(id=cls._kingdom_id)
        except ObjectDoesNotExist:
            raise ValueError(f"Kingdom with the specified ID {cls._kingdom_id} does not exist.")

    def save(self, *args, **kwargs):
        if not self.kingdom:
            self.kingdom = self.get_kingdom()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

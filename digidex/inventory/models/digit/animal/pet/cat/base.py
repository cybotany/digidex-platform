from django.db import models
from digidex.inventory.models.digit.animal.pet import base

class PetCat(base.Pet):
    indoor = models.BooleanField(
        default=True
    )

    def get_kingdom_id(self):
        """
        Return the kingdom ID for animals.
        """
        return 5

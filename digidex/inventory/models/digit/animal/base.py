from digidex.inventory.models.digit import base as base_digit

class Animal(base_digit.Digit):
    """
    A digitized representation of an animal.
    """
    _itis_kingdom_pk = 5
    _itis_rank_pk = 98
    _itis_taxon_pk = 202423
    
    class Meta:
        abstract = True

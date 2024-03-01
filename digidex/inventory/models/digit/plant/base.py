from digidex.inventory.models.digit import base as base_digit

class Plant(base_digit.Digit):
    """
    A digitized representation of a plant
    """
    _itis_kingdom_pk = 3
    _itis_rank_pk = 47
    _itis_taxon_pk = 202422

    class Meta:
        abstract = True

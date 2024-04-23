from digidex.inventory.models.digitized import _digit

class _DigitizedPlant(_digit._Digit):
    """
    A digitized representation of a plant
    """
    _itis_kingdom_pk = 3
    _itis_rank_pk = 47
    _itis_taxon_pk = 202422

    class Meta:
        abstract = True


class DigitizedHousePlant(_DigitizedPlant):
    """
    A digitized representation of a houseplant.
    """

    class Meta:
        verbose_name = "House Plant"
        verbose_name_plural = "House Plants"

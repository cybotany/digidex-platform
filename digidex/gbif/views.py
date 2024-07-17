from queryish.rest import APIModel
from wagtail.admin.viewsets.chooser import ChooserViewSet

from pygbif import species


class GBIFSpecies(APIModel):
    class Meta:
        base_url = "https://api.gbif.org/v1/species/"
        fields = ["key", "scientificName", "rank", "status", "kingdom", "phylum", "class", "order", "family", "genus"]
        pagination_style = "offset-limit"
        limit_query_param = "limit"
        offset_query_param = "offset"

    @classmethod
    def name_backbone(cls, name, **kwargs):
        return species.name_backbone(name=name, **kwargs)
    
    @classmethod
    def name_suggest(cls, q, **kwargs):
        return species.name_suggest(q=q, **kwargs)
    
    @classmethod
    def name_usage(cls, **kwargs):
        return species.name_usage(**kwargs)
    
    @classmethod
    def name_lookup(cls, **kwargs):
        return species.name_lookup(**kwargs)
    
    @classmethod
    def name_parser(cls, name):
        return species.name_parser(name)
    
    def __str__(self):
        return self.scientificName


class SpeciesChooserViewSet(ChooserViewSet):
    model = GBIFSpecies

    choose_one_text = "Choose a species"
    choose_another_text = "Choose another species"


species_chooser_viewset = SpeciesChooserViewSet("species_chooser")

from queryish.rest import APIModel
from queryish.rest import APIQuerySet

from pygbif import species

class SpeciesAPIQuerySet(APIQuerySet):
    
    def run_count(self):
        response_json = self.get_response_json()
        count = response_json.get("count")
        
        if count is None:
            count = len(response_json.get("results", []))
        
        self._count = count
        return count

class Species(APIModel):
    base_query_class = SpeciesAPIQuerySet

    class Meta:
        base_url = "https://api.gbif.org/v1/species/"
        fields = [
            "taxonID", "kingdom", "kingdomKey",
            "scientificName", "canonicalName", "vernacularName",
            "nameType", "rank", "taxonomicStatus",
        ]
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
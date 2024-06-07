from pygbif import species

def get_species_name_suggestions(query, rank=None, limit=20):
    return species.name_suggest(q=query, rank=rank, limit=limit)

def get_species_backbone(name, kingdom=None, rank=None):
    return species.name_backbone(name=name, kingdom=kingdom, rank=rank)

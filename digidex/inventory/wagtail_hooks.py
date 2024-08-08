from wagtail.admin.viewsets.chooser import ChooserViewSet

from inventory.models import Species


class SpeciesChooserViewSet(ChooserViewSet):
    model = Species

    choose_one_text = "Choose a species"
    choose_another_text = "Choose another species"


species_chooser_viewset = SpeciesChooserViewSet("species_chooser")

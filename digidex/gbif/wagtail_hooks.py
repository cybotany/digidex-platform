from wagtail import hooks

from gbif.views import species_chooser_viewset


@hooks.register("register_admin_viewset")
def register_species_chooser_viewset():
    return species_chooser_viewset

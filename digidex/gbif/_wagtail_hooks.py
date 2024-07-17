from wagtail import hooks

from gbif.views import pokemon_chooser_viewset


@hooks.register("register_admin_viewset")
def register_pokemon_chooser_viewset():
    return pokemon_chooser_viewset

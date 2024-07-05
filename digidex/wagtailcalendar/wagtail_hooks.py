from wagtail import hooks

from .views import AgendaViewSetGroup


@hooks.register("register_admin_viewset")
def register_viewset():
    return AgendaViewSetGroup()

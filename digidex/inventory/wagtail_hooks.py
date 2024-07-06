from wagtail import hooks

from inventory.components import WelcomePanel

    
@hooks.register('construct_homepage_panels')
def add_another_welcome_panel(request, panels):
    panels.append(WelcomePanel())

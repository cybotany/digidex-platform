from django import template
from base.models import navbar

register = template.Library()

@register.inclusion_tag("base/includes/navbar/authenticated_action.html", takes_context=True)
def get_authenticated_navbar_buttons(context):
    auth_buttons = navbar.AuthenticatedNavbarButton.objects.all()
    return {'auth_buttons': auth_buttons}

@register.inclusion_tag("base/includes/navbar/non_authenticated_action.html", takes_context=True)
def get_non_authenticated_navbar_buttons(context):
    non_auth_buttons = navbar.NonAuthenticatedNavbarButton.objects.all()
    return {'non_auth_buttons': non_auth_buttons}

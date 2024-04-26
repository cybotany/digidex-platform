from django import template
from wagtail.models import Site

from base.models import header

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page

@register.inclusion_tag("base/includes/header/authenticated_action.html", takes_context=True)
def get_authenticated_navbar_buttons(context):
    auth_buttons = header.AuthenticatedNavbarButton.objects.all()
    return {'auth_buttons': auth_buttons}

@register.inclusion_tag("base/includes/header/non_authenticated_action.html", takes_context=True)
def get_non_authenticated_navbar_buttons(context):
    non_auth_buttons = header.NonAuthenticatedNavbarButton.objects.all()
    return {'non_auth_buttons': non_auth_buttons}

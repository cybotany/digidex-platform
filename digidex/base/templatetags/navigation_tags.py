from django import template
from wagtail.models import Site
from wagtail.contrib.settings.context_processors import SettingsProxy

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page

@register.simple_tag(takes_context=True)
def get_navigation_settings(context):
    site = Site.find_for_request(context['request'])
    settings = SettingsProxy(site)
    return settings.for_site(site).navigationsettings 
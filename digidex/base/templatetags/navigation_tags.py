from django import template

from wagtail import models

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return models.Site.find_for_request(context["request"]).root_page

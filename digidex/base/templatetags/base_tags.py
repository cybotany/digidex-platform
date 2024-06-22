import os

from django import template
from django.utils.text import slugify

from wagtail.models import Site

register = template.Library()

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


@register.simple_tag(takes_context=True)
def get_trainer_page_url(context):
    request = context['request']
    user = request.user

    if user.is_authenticated:
        return os.path.join(
            "/",
            slugify(user.username)
        )
    return None

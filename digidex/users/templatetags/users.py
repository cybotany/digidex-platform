import os

from django import template
from django.utils.text import slugify

register = template.Library()

@register.simple_tag(takes_context=True)
def get_user_profile_url(context):
    request = context['request']
    user = request.user

    if user.is_authenticated:
        return os.path.join(
            "/",
            slugify(user.username)
        )
    return None

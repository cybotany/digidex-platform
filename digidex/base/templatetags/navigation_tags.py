import os

from django import template
from django.utils.text import slugify

from wagtail.models import Site

from base.models.navigation import FooterText

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


@register.inclusion_tag("base/includes/footer/copyright.html", takes_context=True)
def get_footer_copyright(context):
    footer_copyright = context.get("footer_copyright", "")

    if not footer_copyright:
        instance = FooterText.objects.filter(live=True).first()
        footer_copyright = instance.body if instance else ""

    return {
        "footer_copyright": footer_copyright,
    }

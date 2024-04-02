from django import template
from wagtail import models

from base.models import settings as _settings

register = template.Library()

@register.inclusion_tag("includes/footer.html", takes_context=True)
def get_footer(context):
    request = context.get('request')
    site = models.Site.find_for_request(request) if request else None
    social_media = _settings.SocialMediaSettings.for_site(site) if site else _settings.SocialMediaSettings.objects.first()

    return {
        'social_media': social_media,
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return models.Site.find_for_request(context["request"]).root_page


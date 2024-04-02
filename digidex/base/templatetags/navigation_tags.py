from django import template
from wagtail import models

from base.models import settings as _settings

register = template.Library()

@register.inclusion_tag("includes/footer.html", takes_context=True)
def get_footer(context):
    request = context.get('request')
    site = models.Site.find_for_request(request) if request else None
    
    about_us = _settings.AboutUsSettings.for_site(site) if site else _settings.AboutUsSettings.objects.first()
    news_and_events = _settings.NewsAndEventsSettings.for_site(site) if site else _settings.NewsAndEventsSettings.objects.first()
    social_media = _settings.SocialMediaSettings.for_site(site) if site else _settings.SocialMediaSettings.objects.first()

    return {
        'about_us': about_us,
        'news_and_events': news_and_events,
        'social_media': social_media,
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return models.Site.find_for_request(context["request"]).root_page

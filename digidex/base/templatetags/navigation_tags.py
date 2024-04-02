from django import template
from wagtail import models

from base.models import header, footer

register = template.Library()

@register.inclusion_tag("includes/notification_bar.html", takes_context=True)
def get_notification_bar(context):
    request = context.get('request')
    site = models.Site.find_for_request(request) if request else None

    notification_settings = header.NotificationBarSettings.for_site(site) if site else header.NotificationBarSettings.objects.first()

    return {
        'notification_settings': notification_settings,
    }

@register.inclusion_tag("includes/footer.html", takes_context=True)
def get_footer(context):
    # Access the current site from the request
    request = context.get('request')
    site = models.Site.find_for_request(request) if request else None

    footer_settings = footer.FooterSettings.for_site(site) if site else footer.FooterSettings.objects.first()

    return {
        'footer_settings': footer_settings,
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return models.Site.find_for_request(context["request"]).root_page


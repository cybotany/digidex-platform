from django import template
from wagtail.models import Site

from base.models import FooterSettings

register = template.Library()

@register.inclusion_tag("includes/footer.html", takes_context=True)
def get_footer(context):
    # Access the current site from the request
    request = context.get('request')
    site = Site.find_for_request(request) if request else None

    footer_settings = FooterSettings.for_site(site) if site else FooterSettings.objects.first()

    return {
        'footer_settings': footer_settings,
    }


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page

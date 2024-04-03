from django import template
from wagtail import models

from base.models import footer

register = template.Library()

@register.inclusion_tag("base/includes/footer_content.html", takes_context=True)
def get_footer_content(context):
    footer_content = context.get("footer_content", "")

    if not footer_content:
        instance = footer.FooterContent.objects.filter(live=True).first()
        footer_content = instance.paragraph if instance else ""

    return {
        "footer_content": footer_content,
    }

@register.inclusion_tag("base/includes/footer_notice.html", takes_context=True)
def get_footer_notice(context):
    footer_notice = context.get("footer_notice", "")

    if not footer_notice:
        instance = footer.FooterNotice.objects.filter(live=True).first()
        footer_notice = instance.notice if instance else ""

    return {
        "footer_notice": footer_notice,
    }

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return models.Site.find_for_request(context["request"]).root_page

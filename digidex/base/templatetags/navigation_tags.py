from django import template
from wagtail import models

from base.models import footer

register = template.Library()

@register.inclusion_tag("base/includes/footer_content.html", takes_context=True)
def get_footer_content(context):
    DEFAULT_CONTENT = {
        "paragraph": "",
    }

    _content = footer.FooterContent.objects.first()
    footer_content = {
        "paragraph": _content.paragraph if _content else DEFAULT_CONTENT["paragraph"],
    }

    return footer_content

@register.inclusion_tag("base/includes/footer_notice.html", takes_context=True)
def get_footer_notice(context):
    DEFAULT_NOTICE = {
        "notice": "",
    }

    _notice = footer.FooterNotice.objects.first()
    footer_notice = {
        "notice": _notice.notice if _notice else DEFAULT_NOTICE["notice"],
    }

    return footer_notice

@register.simple_tag(takes_context=True)
def get_site_root(context):
    return models.Site.find_for_request(context["request"]).root_page

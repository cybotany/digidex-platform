from django.urls import reverse
from django import template

from wagtail.models import Site

from base.components import SectionComponent, BlockComponent, HeadingComponent, ParagraphComponent


register = template.Library()

def get_inventory(user):
    from inventory.models import InventoryPage
    return InventoryPage.objects.get(owner=user)


@register.inclusion_tag("inventory/includes/header/logo.html", takes_context=True)
def get_header_heading(context):
    return {
        "site_root": Site.find_for_request(context["request"]).root_page,
    }


@register.inclusion_tag("inventory/includes/header/logo.html", takes_context=True)
def get_header_paragraph(context):
    return {
        "site_root": Site.find_for_request(context["request"]).root_page,
    }


@register.inclusion_tag("inventory/includes/header/logo.html", takes_context=True)
def get_header_categories(context):
    return {
        "site_root": Site.find_for_request(context["request"]).root_page,
    }

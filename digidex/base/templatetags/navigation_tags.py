from django import template
from django.urls import reverse

from wagtail.models import Site

from base.models import SiteLogo, FooterParagraph, FooterCopyright
from base.components import ParagraphComponent, ButtonComponent, LinkComponent


register = template.Library()

def get_inventory(user):
    from inventory.models import UserInventoryIndex
    return UserInventoryIndex.objects.get(owner=user)


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


@register.simple_tag(takes_context=True)
def get_site_logo(context):
    instance = SiteLogo.objects.first()
    digidex_logo = instance.logo if instance else ""
    return digidex_logo


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


@register.inclusion_tag("base/includes/footer/paragraph.html", takes_context=True)
def get_footer_paragraph(context):
    paragraph = context.get("footer_paragraph", "")

    if not paragraph:
        instance = FooterParagraph.objects.filter(live=True).first()
        paragraph = instance.paragraph if instance else ""

    footer_paragraph = ParagraphComponent(
        text=paragraph,
        line_break=True,
        style='footer'
    )

    return {
        "footer_paragraph": footer_paragraph,
    }


@register.inclusion_tag("base/includes/footer/copyright.html", takes_context=True)
def get_footer_copyright(context):
    footer_copyright = context.get("footer_copyright", "")

    if not footer_copyright:
        instance = FooterCopyright.objects.filter(live=True).first()
        footer_copyright = instance.copyright if instance else "All rights reserved."

    return {
        "footer_copyright": footer_copyright,
    }


@register.inclusion_tag("base/includes/navigation/links.html", takes_context=True)
def get_navigation_links(context):
    links = []

    request = context["request"]
    if request.user.is_authenticated:
        inventory = get_inventory(request.user)
        #party = inventory.get_party()
        #items = party.get_items()

        items = []
        for item in items:
            links.append(
                LinkComponent(
                    url = item.url,
                    text = item.name,
                    style = 'nav'
                )
            )

    return {
        "links": links,
    }


@register.inclusion_tag("base/includes/navigation/buttons.html", takes_context=True)
def get_navigation_buttons(context):
    request = context["request"]
    if request.user.is_authenticated:
        buttons = [
            ButtonComponent(
                text='Email',
                url=reverse("account_email"),
                style='nav-button-outline'
            ),
            ButtonComponent(
                text='Password',
                url=reverse("account_change_password"),
                style='nav-button-outline'
            ),
            ButtonComponent(
                text='Logout',
                url=reverse("account_logout"),
                style='nav-button'
            )
        ]   
    else:
        buttons = [
            ButtonComponent(
                text='Login',
                url=reverse("account_login"),
                style='nav-button-outline'
            ),
            ButtonComponent(
                text='Signup',
                url=reverse("account_signup"),
                style='nav-button'
            )
        ]
    return {
            "buttons": buttons,
        }

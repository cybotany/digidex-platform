from django import template
from django_hosts.resolvers import reverse

from wagtail.models import Site

from base.components import ButtonComponent, LinkComponent


register = template.Library()

def get_inventory(user):
    from inventory.models import UserInventoryIndex
    return UserInventoryIndex.objects.get(owner=user)


@register.inclusion_tag("base/includes/navigation/logo.html", takes_context=True)
def get_navigation_logo(context):
    return {
        "site_root": Site.find_for_request(context["request"]).root_page.url,
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
                url=reverse("account_email", host='account'),
                style='nav-button-outline'
            ),
            ButtonComponent(
                text='Password',
                url=reverse("account_change_password", host='account'),
                style='nav-button-outline'
            ),
            ButtonComponent(
                text='Logout',
                url=reverse("account_logout", host='account'),
                style='nav-button'
            )
        ]   
    else:
        buttons = [
            ButtonComponent(
                text='Login',
                url=reverse("account_login", host='account'),
                style='nav-button-outline'
            ),
            ButtonComponent(
                text='Signup',
                url=reverse("account_signup", host='account'),
                style='nav-button'
            )
        ]
    return {
            "buttons": buttons,
        }

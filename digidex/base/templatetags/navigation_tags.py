from django import template
from wagtail.models import Site

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


@register.inclusion_tag('breadcrumbs.html', takes_context=True)
def breadcrumbs(context):
    page = context.get('page')
    if not page:
        return {'breadcrumbs': []}

    breadcrumbs = []
    while page:
        breadcrumbs.insert(0, page)
        page = page.get_parent()
    
    return {'breadcrumbs': breadcrumbs}

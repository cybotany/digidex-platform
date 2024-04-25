from django import template
from base.models import footer

register = template.Library()

@register.inclusion_tag("base/includes/footer/information.html", takes_context=True)
def get_footer_information(context):
    information = footer.FooterInformation.objects.filter().first()
    if not information:
        information = {
            'paragraph': '',
            'phone_number': '',
            'email': '',
            'chat': ''
        }
    else:
        information = {
            'paragraph': information.paragraph,
            'phone_number': information.phone_number,
            'email': information.email,
            'chat': information.chat
        }
    
    return information

@register.inclusion_tag("base/includes/footer/internal_links.html", takes_context=True)
def get_footer_internal_links(context):
    internal_links = footer.FooterInternalLinks.objects.filter().first()
    if not internal_links:
        internal_links = {
            'blog': '',
            'company': '',
            'solutions': '',
            'support':  ''
        }
    else:
        internal_links = {
            'blog': internal_links.blog,
            'company': internal_links.company,
            'solutions': internal_links.solutions,
            'support': internal_links.support
        }
    
    return internal_links


@register.inclusion_tag("base/includes/footer/social_links.html", takes_context=True)
def get_footer_social_links(context):
    social_links = footer.FooterSocialLinks.objects.filter().first()
    if not social_links:
        social_links = {
            'github': '',
            'twitter':  ''
        }
    else:
        social_links = {
            'github': social_links.github,
            'twitter': social_links.twitter
        }
    
    return social_links


@register.inclusion_tag("base/includes/footer/social_links.html", takes_context=True)
def get_footer_social_links(context):
    instance = footer.FooterCopyright.objects.filter().first()
    footer_copyright = instance.copyright if instance else ""
    
    return {
        'footer_copyright': footer_copyright
    }

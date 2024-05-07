from django import template

from base.models import footer

register = template.Library()


@register.inclusion_tag("base/includes/footer/paragraph.html", takes_context=True)
def get_footer_paragraph(context):
    footer_paragraph = context.get("footer_paragraph", "")

    if not footer_paragraph:
        instance = footer.FooterParagraph.objects.filter(live=True).first()
        footer_paragraph = instance.paragraph if instance else "Footer Paragraph Placeholder"

    return {
        "footer_paragraph": footer_paragraph
    }


@register.inclusion_tag("base/includes/footer/copyright.html", takes_context=True)
def get_footer_copyright(context):
    footer_copyright = context.get("footer_copyright", "")

    if not footer_copyright:
        instance = footer.FooterCopyright.objects.filter(live=True).first()
        footer_copyright = instance.copyright if instance else "All Rights Reserved"

    return {
        "footer_copyright": footer_copyright
    }

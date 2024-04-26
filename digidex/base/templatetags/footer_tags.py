from django import template
from base.models import footer

register = template.Library()

@register.inclusion_tag("base/includes/footer/paragraph.html", takes_context=True)
def get_footer_paragraph(context):
    instance = footer.FooterParagraph.objects.filter().first()
    if not instance:
        instance = {
            'paragraph': 'Footer Paragraph Placeholder',
        }
    else:
        instance = {
            'paragraph': instance.paragraph
        }
    
    return instance


@register.inclusion_tag("base/includes/footer/copyright.html", takes_context=True)
def get_footer_copyright(context):
    instance = footer.FooterCopyright.objects.filter().first()
    if not instance:
        copyright = {
            'copyright':  'All Rights Reserved'
        }
    else:
        copyright = {
            'copyright': instance.text
        }
    
    return copyright

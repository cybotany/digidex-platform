from django import template

from digidex.base.models.footer import PageFooter

register = template.Library()

@register.inclusion_tag('tags/footer.html')
def render_footer():
    return {
        'footer': PageFooter.objects.first()
        }

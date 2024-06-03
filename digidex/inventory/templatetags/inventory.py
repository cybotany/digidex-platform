from django import template
from inventory.models import UserProfilePage

register = template.Library()

@register.simple_tag(takes_context=True)
def get_user_profile_url(context):
    request = context['request']
    user = request.user

    if user.is_authenticated:
        try:
            profile_page = UserProfilePage.objects.get(owner=user)
            return profile_page.url
        except UserProfilePage.DoesNotExist:
            return None
    return None

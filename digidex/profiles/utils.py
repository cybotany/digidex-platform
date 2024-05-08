from django.utils.text import slugify

from profiles.models import UserProfile


def create_user_profile(user):
    """
    Create a user profile if it doesn't exist.
    """
    user_slug = slugify(user.username)
    profile, created = UserProfile.objects.get_or_create(
        user=user,
        defaults={'slug': user_slug}
    )
    if created:
        profile.save()
    return profile

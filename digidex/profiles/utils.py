from profiles.models import UserProfile


def create_user_profile(user):
    """
    Create a user profile if it doesn't exist.
    """
    profile, created = UserProfile.objects.get_or_create(user=user)
    if created:
        profile.save()
    return profile

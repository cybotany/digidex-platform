from django.apps import apps
from wagtail.models import Page


def get_or_create_user_profile_index_page():
    try:
        UserProfileIndexPage = apps.get_model('inventory', 'UserProfileIndexPage')
        return UserProfileIndexPage.objects.get(slug='u')
    except UserProfileIndexPage.DoesNotExist:
        root_page = Page.objects.get(url_path='/home/')
        user_index_page = UserProfileIndexPage(
            title='Users',
            slug='u',
            heading='User Profiles',
            intro='Welcome to the user section.'
        )
        root_page.add_child(instance=user_index_page)
        user_index_page.save_revision().publish()
        return None


def get_or_create_user_profile_page(user_profile):
    """
    Create a user page for the given user.
    """
    user_index_page = get_or_create_user_profile_index_page()

    UserProfilePage = apps.get_model('inventory', 'UserProfilePage')
    if not UserProfilePage.objects.filter(profile=user_profile).exists():
        user_profile_page = UserProfilePage(
            title=f"{user_profile._name}'s Profile",
            slug=user_profile.slug,
            owner=user_profile.user,
            profile=user_profile,
        )
        user_index_page.add_child(instance=user_profile_page)
        user_profile_page.save_revision().publish()
        return user_profile_page
    else:
        return UserProfilePage.objects.get(profile=user_profile)

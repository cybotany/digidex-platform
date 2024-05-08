from django.utils.text import slugify
from wagtail.models import Page

from profiles.models import UserProfileIndexPage, UserProfile


def create_user_profile_index_page():
    # Get the root page where 'HomePage' is a direct child of the root
    root_page = Page.objects.get(url_path='/home/')

    # Check if the 'Users' page already exists to avoid duplicates
    if not UserProfileIndexPage.objects.filter(slug='u').exists():
        user_profile_index_page = UserProfileIndexPage(
            title='Users',
            slug='u',
            heading='User Profiles',
            intro='Welcome to the user profiles section.'
        )
        root_page.add_child(instance=user_profile_index_page)
        user_profile_index_page.save_revision().publish()

        print('UserProfileIndexPage created and added successfully!')
    else:
        print('UserProfileIndexPage already exists.')


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

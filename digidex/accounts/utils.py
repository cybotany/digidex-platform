from django.utils.text import slugify

from wagtail.models import Page

from accounts.models import UserIndexPage, UserProfile


def create_user_profile_index_page():
    root_page = Page.objects.get(url_path='/home/')

    if not UserIndexPage.objects.filter(slug='u').exists():
        user_index_page = UserIndexPage(
            title='Users',
            slug='u',
            heading='User Profiles',
            intro='Welcome to the user section.'
        )
        root_page.add_child(instance=user_index_page)
        user_index_page.save_revision().publish()

        print('UserIndexPage created and added successfully!')
    else:
        print('UserIndexPage already exists.')


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

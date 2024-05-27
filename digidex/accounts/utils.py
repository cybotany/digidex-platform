from wagtail.models import Page

from accounts.models import UserIndexPage


def create_user_index_page():
    """
    Create a user index page if it doesn't exist.
    """
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


def create_user_page(user):
    """
    Create a user page for the given user.
    """
    return user.create_page()


def create_user_profile(user):
    """
    Create a user profile for the given user.
    """
    return user.create_profile()

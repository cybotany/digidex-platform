from django.apps import apps
from wagtail.models import Page


def get_or_create_user_profile_index_page():
    
    UserProfileIndexPage = apps.get_model('inventory', 'UserProfileIndexPage')
    if not UserProfileIndexPage.objects.filter(slug='u').exists():
        root_page = Page.objects.get(url_path='/home/')
        user_index_page = UserProfileIndexPage(
            title='Users',
            slug='u',
            heading='User Profiles',
            intro='Welcome to the user section.'
        )
        root_page.add_child(instance=user_index_page)
        user_index_page.save_revision().publish()
    else:
        user_index_page = UserProfileIndexPage.objects.get(slug='u')
    return user_index_page


def get_or_create_user_profile_page(user):
    """
    Create a user page for the given user.
    """
    UserProfilePage = apps.get_model('inventory', 'UserProfilePage')
    if not UserProfilePage.objects.filter(profile=user).exists():
        user_profile_page = UserProfilePage(
            title=f"{user.username.title()}'s Profile",
            slug=user.user.base_slug,
            owner=user.user,
            profile=user,
        )
        user_index_page = get_or_create_user_profile_index_page()
        user_index_page.add_child(instance=user_profile_page)
        user_profile_page.save_revision().publish()
    else:
        user_profile_page = UserProfilePage.objects.get(profile=user)
    return user_profile_page


def get_or_create_inventory_category_page(category):
    """
    Create a user page for the given user.
    """
    CategoryPage = apps.get_model('inventory', 'CategoryPage')    
    if not CategoryPage.objects.filter(category=category).exists():
        category_page = CategoryPage(
            title=category.name,
            slug=category.base_slug,
            owner=category.user,
            category=category
        )

        parent_page = get_or_create_user_profile_page(category.user.profile)
        parent_page.add_child(instance=category_page)
        category_page.save_revision().publish()
    else:
        category_page = CategoryPage.objects.get(category=category)
    return category_page

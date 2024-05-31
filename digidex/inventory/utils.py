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


def get_or_create_user_profile(user):
    """
    Create a user profile for the given user.
    """
    UserProfile = apps.get_model('inventory', 'UserProfile')
    if not UserProfile.objects.filter(user=user).exists():
        user_profile = UserProfile(user=user)
        user_profile.save()
    else:
        user_profile = UserProfile.objects.get(user=user)
    return user_profile


def get_or_create_user_profile_page(user_profile):
    """
    Create a user page for the given user.
    """
    UserProfilePage = apps.get_model('inventory', 'UserProfilePage')
    if not UserProfilePage.objects.filter(profile=user_profile).exists():
        user_profile_page = UserProfilePage(
            title=f"{user_profile._name}'s Profile",
            slug=user_profile.slug,
            owner=user_profile.user,
            user_profile=user_profile,
        )
        user_index_page = get_or_create_user_profile_index_page()
        user_index_page.add_child(instance=user_profile_page)
        user_profile_page.save_revision().publish()
    else:
        user_profile_page = UserProfilePage.objects.get(profile=user_profile)
    return user_profile_page


def get_or_create_inventory_category_page(category):
    """
    Create a user page for the given user.
    """
    InventoryCategoryPage = apps.get_model('inventory', 'InventoryCategoryPage')    
    if not InventoryCategoryPage.objects.filter(category=category).exists():
        category_page = InventoryCategoryPage(
            title=category.name,
            slug=category.slug,
            owner=category.user_profile.user,
            category=category
        )

        parent_page = get_or_create_user_profile_page(category.user_profile)
        parent_page.add_child(instance=category_page)
        category_page.save_revision().publish()
    else:
        category_page = InventoryCategoryPage.objects.get(category=category)
    return category_page


def get_or_create_inventory_digit_page(digit):
    """
    Create a user page for the given user.
    """
    InventoryDigitPage = apps.get_model('inventory', 'InventoryDigitPage')
    if not InventoryDigitPage.objects.filter(digit=digit).exists():
        digit_page = InventoryDigitPage(
            title=digit.name,
            slug=digit.slug,
            owner=digit.user_profile.user,
            digit=digit
        )

        parent_page = get_or_create_inventory_category_page(digit.category)
        parent_page.add_child(instance=digit_page)
        digit_page.save_revision().publish()
    else:
        digit_page = InventoryDigitPage.objects.get(digit=digit)
    return digit_page


def get_or_create_inventory_digit_journal(digit):
    """
    Create a journal for the given digit.
    """
    EntryCollection = apps.get_model('journal', 'EntryCollection')
    if not EntryCollection.objects.filter(digit=digit).exists():
        journal = EntryCollection.objects.create(
            digit=digit
        )
    else:
        journal = EntryCollection.objects.get(digit=digit)
    return journal

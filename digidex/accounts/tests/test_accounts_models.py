import pytest
from wagtail.models import Collection, GroupCollectionPermission

from accounts.models import UserProfile, UserProfilePage

@pytest.mark.django_db
def test_create_user_group(new_user):
    # Initially, the user should not be in any group
    assert new_user.groups.count() == 0
    
    # Create user group and check if it's created
    created = new_user.create_user_group()
    assert created is True
    assert new_user.groups.count() == 1
    assert new_user.groups.first().name == f"user_{new_user.username}_group"
    
    # Calling it again should not create a new group, and 'created' should be False
    created_again = new_user.create_user_group()
    assert created_again is False
    assert new_user.groups.count() == 1  # No new group should be added

@pytest.mark.django_db
def test_set_collection_permissions(new_user):
    # Setup a collection
    collection = Collection.objects.create(name="Test Collection")

    # Check no permissions initially
    assert new_user.groups.first() is None
    
    # Set permissions and validate
    new_user.create_user_group()  # Ensure the user has a group
    new_user.set_collection_permissions(collection)
    
    # Get the group again
    group = new_user.groups.first()
    
    # Check if permissions are set
    for permission in ['add', 'change', 'delete', 'view']:
        permission_codename = f'{permission}_{collection._meta.model_name}'
        assert GroupCollectionPermission.objects.filter(
            group=group, 
            permission__codename=permission_codename
        ).exists()

@pytest.mark.django_db
def test_create_user_profile_page(new_user):
    # Create user profile
    profile = UserProfile.objects.create(user=new_user)
    
    # Create profile page
    profile_page = profile.create_user_profile_page()
    
    # Check if the profile page is created and linked
    assert profile_page.title == f"{new_user.username}'s Profile"
    assert profile_page.owner == new_user
    assert UserProfilePage.objects.filter(owner=new_user).exists()

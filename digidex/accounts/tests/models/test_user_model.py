import pytest
from wagtail.models import Collection

from accounts.models import UserCollection

@pytest.mark.django_db
def test_create_user_collection(new_user):
    # Precondition: Ensure there is no collection named "Users" initially
    assert Collection.objects.filter(name='Users').count() == 0

    # Call the method to test
    user_collection = new_user.create_user_collection()

    # Check that the root collection 'Users' is created
    users_root = Collection.objects.get(name='Users')
    assert users_root is not None
    assert users_root.depth == 1  # assuming 'Users' is at root depth

    # Check that the user collection is created under 'Users'
    assert user_collection.name == f"{new_user.username}'s Collection"
    assert user_collection.get_parent() == users_root

@pytest.mark.django_db
def test_create_user_collection_idempotent(new_user):
    # Call the create_user_collection method twice
    collection1 = new_user.create_user_collection()
    collection2 = new_user.create_user_collection()

    # Check that calling it a second time does not create a new collection
    assert collection1 == collection2
    assert Collection.objects.filter(name=f"{new_user.username}'s Collection").count() == 1

    # Assert: Check the total number of collections named "Users"
    assert Collection.objects.filter(name='Users').count() == 1

@pytest.mark.django_db
def test_create_user_collection_links_to_user(new_user):
    # Act: Create user collection
    user_collection = new_user.create_user_collection()

    # Assert: Check that a UserCollection entry is created linking the user to the collection
    user_collection_link = UserCollection.objects.get(user=new_user)
    assert user_collection_link.collection == user_collection
    assert user_collection.name == f"{new_user.username}'s Collection"

    # Assert that the link is unique
    assert UserCollection.objects.filter(user=new_user).count() == 1

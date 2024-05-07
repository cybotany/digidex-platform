import pytest
from django.db.models import Count
from wagtail.models import Collection

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

    # Check that the collection is indeed linked to the user somehow if applicable
    # This is optional and depends on your application design
    # For example, you might want to check if there's a foreign key from collection to user

@pytest.mark.django_db
def test_create_user_collection_idempotent(new_user):
    # Call the create_user_collection method twice
    collection1 = new_user.create_user_collection()
    collection2 = new_user.create_user_collection()

    # Check that calling it a second time does not create a new collection
    assert collection1 == collection2
    assert Collection.objects.filter(name=f"{new_user.username}'s Collection").count() == 1

    # Optional: Check the total number of collections named "Users"
    assert Collection.objects.filter(name='Users').count() == 1

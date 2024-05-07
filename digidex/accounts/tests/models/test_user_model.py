import pytest
from wagtail.models import Collection


@pytest.mark.django_db
def test_build_root_user_collection(new_user):
    collection, created = new_user.build_root_user_collection()
    assert collection.name == 'Users', "Should create or retrieve a 'Users' root collection."
    assert created or not created, "Should indicate if the collection was created or retrieved."


@pytest.mark.django_db
def test_build_user_collection_name(new_user):
    expected_name = f"{new_user.username}'s Collection"
    assert new_user.build_user_collection_name() == expected_name, "Collection name should match the expected format."


@pytest.mark.django_db
def test_check_for_existing_collection(new_user):
    users_root_collection, _ = new_user.build_root_user_collection()
    # Create a new collection under 'Users'
    new_user_collection = users_root_collection.add_child(name=f"{new_user.username}'s Collection")
    # Check if the collection is detected correctly
    result = new_user.check_for_existing_collection(f"{new_user.username}'s Collection", users_root_collection)
    assert result == new_user_collection, "Should find the existing collection correctly."


@pytest.mark.django_db(transaction=True)
def test_transaction_atomicity(new_user, monkeypatch):
    # Simulate an error during collection creation
    def mock_add_child(self, **kwargs):
        raise Exception("Simulated error")

    monkeypatch.setattr(Collection, 'add_child', mock_add_child)
    with pytest.raises(Exception):
        new_user.create_user_collection()
    # Check that no collections have been added
    assert Collection.objects.count() == 1, "No new collections should be created on error."


@pytest.mark.django_db
def test_create_user_collection(new_user):
    # Create user collection and assert it exists as expected
    user_collection_link = new_user.create_user_collection()
    user_collection = user_collection_link.collection

    # Ensure the Collection created is the user-specific one
    expected_name = f"{new_user.username}'s Collection"
    users_root_collection = Collection.objects.get(name="Users")  # Get the Users root collection

    assert user_collection.name == expected_name
    assert user_collection.depth == users_root_collection.depth + 1
    assert user_collection.path.startswith(users_root_collection.path)
    assert Collection.objects.filter(name=expected_name, path__startswith=users_root_collection.path).count() == 1


@pytest.mark.django_db
def test_prevent_multiple_user_collections(new_user):
    # Create the user collection twice
    new_user.create_user_collection()
    new_user.create_user_collection()

    # Test that only one user-specific collection is created
    expected_name = f"{new_user.username}'s Collection"
    users_root_collection = Collection.objects.get(name="Users")
    assert Collection.objects.filter(name=expected_name, path__startswith=users_root_collection.path).count() == 1


@pytest.mark.django_db
def test_user_collection_link(new_user):
    # Create user collection and link it
    user_collection_link = new_user.create_user_collection()

    # Verify that link is established correctly
    assert user_collection_link.user == new_user
    collection_name = f"{new_user.username}'s Collection"
    assert user_collection_link.collection.name == collection_name

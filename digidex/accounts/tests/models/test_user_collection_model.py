import pytest
from wagtail.models import Collection


@pytest.mark.django_db
def test_create_user_collection(new_user):
    user_collection_link = new_user.create_user_collection()
    user_collection = user_collection_link.collection

    expected_name = f"{new_user.username}'s Collection"
    users_root_collection = Collection.objects.get(name="Users")

    assert user_collection.name == expected_name
    assert user_collection.depth == users_root_collection.depth + 1
    assert user_collection.path.startswith(users_root_collection.path)
    assert Collection.objects.filter(name=expected_name, path__startswith=users_root_collection.path).count() == 1


@pytest.mark.django_db
def test_prevent_multiple_user_collections(new_user):
    new_user.create_user_collection()
    new_user.create_user_collection()

    expected_name = f"{new_user.username}'s Collection"
    users_root_collection = Collection.objects.get(name="Users")
    assert Collection.objects.filter(name=expected_name, path__startswith=users_root_collection.path).count() == 1


@pytest.mark.django_db
def test_user_collection_link(new_user):
    user_collection_link = new_user.create_user_collection()

    assert user_collection_link.user == new_user
    collection_name = f"{new_user.username}'s Collection"
    assert user_collection_link.collection.name == collection_name

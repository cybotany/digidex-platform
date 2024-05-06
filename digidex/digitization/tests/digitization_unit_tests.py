import pytest
from django.test import TestCase
from django.utils import timezone

from accounts.models import User
from digitization.models import DigitizedObject
from inventory.models import UserDigitizedObject


@pytest.fixture
def test_user(db):
    return User.objects.create(username='testuser', password='testpass123')

@pytest.fixture
def digitized_object(db):
    return DigitizedObject.objects.create(
        name="Ancient Manuscript",
        description="Detailed description of the manuscript."
    )

def test_digitized_object_creation(digitized_object):
    """ Test the creation of a DigitizedObject and validate its properties. """
    assert digitized_object.uuid is not None
    assert digitized_object.name == "Ancient Manuscript"
    assert digitized_object.description == "Detailed description of the manuscript."
    assert isinstance(digitized_object.created_at, timezone.datetime)
    assert isinstance(digitized_object.last_modified, timezone.datetime)

def test_digitized_object_str_representation(digitized_object):
    """ Test the string representation of the DigitizedObject. """
    assert str(digitized_object) == "Ancient Manuscript"

def test_set_user_association(digitized_object, test_user, db):
    """ Test the set_user_association method. """
    association = digitized_object.set_user_association(test_user)
    assert association.user == test_user
    assert association.digit == digitized_object

def test_get_user_association(digitized_object, test_user, db):
    """ Test retrieving the user association. """
    DigitizedObject.objects.create(name="Another Object")
    association = digitized_object.set_user_association(test_user)
    retrieved_association = digitized_object.get_user_association()
    assert retrieved_association == association

def test_get_associated_page_url_no_association(digitized_object, db):
    """ Test the get_associated_page_url method when there is no associated page. """
    assert digitized_object.get_associated_page_url() is None

def test_error_handling_get_user_association(digitized_object, db):
    """ Test error handling for get_user_association when no association exists. """
    with pytest.raises(UserDigitizedObject.DoesNotExist):
        digitized_object.get_user_association()

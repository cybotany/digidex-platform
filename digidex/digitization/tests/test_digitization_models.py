import pytest
from django.utils import timezone

from digitization.models import DigitizedObject
from inventory.models import UserDigitizedObject

def test_digitized_object_creation(digitized_object, db):
    """ Test the creation of a DigitizedObject and validate its properties. """
    assert digitized_object.uuid is not None
    assert digitized_object.name == "Kira"
    assert digitized_object.description == "Cream Shiba Inu with a curly tail."
    assert isinstance(digitized_object.created_at, timezone.datetime)
    assert isinstance(digitized_object.last_modified, timezone.datetime)

def test_digitized_object_str_representation(digitized_object, db):
    """ Test the string representation of the DigitizedObject. """
    assert str(digitized_object) == "Kira"

def test_set_user_association(digitized_object, user, db):
    """ Test the set_user_association method. """
    association = digitized_object.set_user_association(user)
    assert association.user == user
    assert association.digit == digitized_object

def test_get_user_association(digitized_object, user, db):
    """ Test retrieving the user association. """
    DigitizedObject.objects.create(name="Another Object")
    association = digitized_object.set_user_association(user)
    retrieved_association = digitized_object.get_user_association()
    assert retrieved_association == association

def test_get_associated_page_url_no_association(digitized_object, db):
    """ Test the get_associated_page_url method when there is no associated page. """
    assert digitized_object.get_associated_page_url() is None

def test_error_handling_get_user_association(digitized_object, db):
    """ Test error handling for get_user_association when no association exists. """
    with pytest.raises(UserDigitizedObject.DoesNotExist):
        digitized_object.get_user_association()
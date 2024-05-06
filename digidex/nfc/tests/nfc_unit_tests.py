import pytest
from django.core.exceptions import ValidationError

from nfc.models import NearFieldCommunicationTag
from digitization.models import DigitizedObject

@pytest.fixture
def digitized_object(db):
    return DigitizedObject.objects.create(
        name="Sample Object",
        description="A sample digitized object."
    )

@pytest.fixture
def ntag(db, digitized_object):
    return NearFieldCommunicationTag.objects.create(
        serial_number='1234567890ABCDEF',
        digitized_object=digitized_object,
        active=False
    )

def test_create_ntag(ntag):
    assert ntag.serial_number == '1234567890ABCDEF'
    assert not ntag.active

def test_activate_link(ntag):
    ntag.activate_link()
    assert ntag.active

def test_deactivate_link(ntag):
    ntag.activate_link()
    ntag.deactivate_link()
    assert not ntag.active

def test_get_digitized_object(ntag):
    assert ntag.get_digitized_object() == ntag.digitized_object

def test_get_digitized_object_without_digitized_object(db):
    ntag = NearFieldCommunicationTag.objects.create(
        serial_number='9876543210FEDCBA',
        active=False
    )
    with pytest.raises(ValidationError):
        ntag.get_digitized_object()

def test_get_absolute_url(ntag):
    url = ntag.get_absolute_url()
    assert url == f"/nfc/{ntag.uuid}/"

def test_get_digitized_object_url(ntag):
    assert ntag.get_digitized_object_url() == ntag.digitized_object.get_associated_page_url()

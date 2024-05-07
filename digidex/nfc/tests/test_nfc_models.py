import pytest
from django.core.exceptions import ValidationError

from nfc.models import NearFieldCommunicationTag


def test_activate_link(ntag):
    ntag.activate_link()
    assert ntag.active


def test_deactivate_link(ntag):
    ntag.activate_link()
    ntag.deactivate_link()
    assert not ntag.active


def test_get_digitized_object(ntag):
    assert ntag.get_digitized_object() == ntag.digitized_object


def test_get_digitized_object_without_digitized_object(ntag_without_digitized_object):
    with pytest.raises(ValidationError):
        ntag_without_digitized_object.get_digitized_object()


def test_get_absolute_url(ntag):
    url = ntag.get_absolute_url()
    assert url == f"/nfc/{ntag.uuid}/"


def test_get_digitized_object_url(ntag):
    assert ntag.get_digitized_object_url() == ntag.digitized_object.get_associated_page_url()


def test_valid_serial_number(ntag):
    assert ntag.serial_number == '01:23:45:67:89:AB:CD'


def test_invalid_serial_number(db):
    with pytest.raises(ValidationError):
        NearFieldCommunicationTag.objects.create(
            serial_number='01:23:45:6789:AB:CD:EF:01:10',
            ntag_type='NTAG 213',
            active=False
        )


def test_valid_ntag_type(ntag):
    assert ntag.ntag_type == 'NTAG 213'


def test_invalid_ntag_type(db):
    with pytest.raises(ValidationError):
        NearFieldCommunicationTag.objects.create(
            serial_number='01:23:45:67:89:AB:CD',
            ntag_type='Invalid Type',
            active=False
        )

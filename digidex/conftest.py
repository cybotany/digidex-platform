import uuid
import pytest
from django.test import Client

from accounts.models import User
from nfc.models import NearFieldCommunicationTag
from digitization.models import DigitizedObject

@pytest.fixture
def user(db):
    return User.objects.create_user(username='test_pet_owner', password='testpass123')

@pytest.fixture
def digitized_object(db):
    return DigitizedObject.objects.create(
        name="Kira",
        description="Cream Shiba Inu with a curly tail."
    )

@pytest.fixture
def ntag(db, digitized_object):
    return NearFieldCommunicationTag.objects.create(
        serial_number='01:23:45:67:89:AB:CD',
        digitized_object=digitized_object,
        active=False
    )

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def active_nfc_tag(db):
    return NearFieldCommunicationTag.objects.create(uuid='127611e2-1f20-4b01-b9eb-390360e04b6b', active=True)

@pytest.fixture
def inactive_nfc_tag(db):
    return NearFieldCommunicationTag.objects.create(uuid='127611e2-1f20-4b01-b9eb-390360e04b6b', active=False)

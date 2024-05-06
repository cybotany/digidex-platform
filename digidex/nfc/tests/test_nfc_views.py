from django.urls import reverse

from nfc.models import NearFieldCommunicationTag

def test_inactive_ntag_returns_403(client, inactive_nfc_tag):
    url = reverse('nfc:route_ntag', kwargs={'_uuid': inactive_nfc_tag.uuid})
    response = client.get(url)
    assert response.status_code == 403

def test_active_ntag_redirects_to_digitized_object(client, active_nfc_tag, mocker):
    mocker.patch.object(NearFieldCommunicationTag, 'get_digitized_object_url', return_value="http://example.com/digit_page")
    active_nfc_tag.digitized_object = mocker.MagicMock()
    active_nfc_tag.save()

    url = reverse('nfc:route_ntag', kwargs={'_uuid': active_nfc_tag.uuid})
    response = client.get(url)
    assert response.status_code == 302
    assert response['Location'] == "http://example.com/digit_page"

def test_active_ntag_redirects_to_link_ntag_when_no_digitized_object(client, active_nfc_tag):
    url = reverse('nfc:route_ntag', kwargs={'_uuid': active_nfc_tag.uuid})
    response = client.get(url)
    assert response.status_code == 302
    assert response['Location'] == reverse('digitization:link_ntag', kwargs={'ntag_uuid': active_nfc_tag.uuid})
from django.urls import reverse


def test_inactive_ntag_returns_403(client, inactive_nfc_tag):
    url = reverse('nfc:route_ntag', kwargs={'_uuid': inactive_nfc_tag.uuid})
    response = client.get(url)
    assert response.status_code == 403


def test_active_ntag_redirects_to_link_ntag_when_no_digitized_object(client, active_nfc_tag):
    url = reverse('nfc:route_ntag', kwargs={'_uuid': active_nfc_tag.uuid})
    response = client.get(url)
    assert response.status_code == 302
    assert response['Location'] == reverse('digitization:link_ntag', kwargs={'ntag_uuid': active_nfc_tag.uuid})

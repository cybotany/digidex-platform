import pytest
from django.urls import reverse
from cybotany.views import HomeView

@pytest.mark.django_db
def test_home_view_contains_signup_link(client):
    url = reverse('home')
    response = client.get(url)
    assert 'id="signup-link"' in str(response.content)

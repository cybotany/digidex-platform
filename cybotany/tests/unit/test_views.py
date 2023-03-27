import pytest
from django.urls import reverse
from django.test import TestCase, RequestFactory
from cybotany.views.SignupView import signup

class TestSignupView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_signup_view_post_redirects_to_signup_info(self):
        # Create a test user data
        user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'TestPassword123',
            'password2': 'TestPassword123',
        }

        # Create a POST request
        request = self.factory.post(reverse('signup'), data=user_data)

        # Call the post() method of SignupView
        response = signup(request)

        # Check if the user is redirected to the signup info page
        self.assertRedirects(response, reverse('signup_info'))




@pytest.mark.django_db
def test_home_view_contains_signup_link(client):
    url = reverse('home')
    response = client.get(url)
    assert 'id="signup-link"' in str(response.content)

import pytest
from django.urls import reverse
from django.test import TestCase, Client
from django.contrib.auth.models import User

class TestSignupView(TestCase):

    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')

    def test_user_is_saved(self):
            """
            Test that a new user is created after submitting the signup form with valid data.
            """
            user_data = {
                'username': 'valid_username',
                'password1': 'ValidPassword123!',
                'password2': 'ValidPassword123!',
            }

            response = self.client.post(self.signup_url, data=user_data)
            self.assertEqual(response.status_code, 302)  # Expecting a redirect after successful signup

            user = User.objects.filter(username='valid_username').first()
            self.assertIsNotNone(user)  # Check if the user is created
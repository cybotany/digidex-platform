import pytest
from django.urls import reverse
from django.test import TestCase, RequestFactory
from cybotany.views.account_signup_view import signup

class TestSignupView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()


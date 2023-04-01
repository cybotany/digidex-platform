import pytest
from django.urls import reverse
from django.test import TestCase, RequestFactory
from cybotany.views.SignupView import signup

class TestSignupView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()


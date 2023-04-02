import pytest
from django.urls import reverse
from django.test import TestCase, RequestFactory

class TestSignupView(TestCase):

    def setUp(self):
        self.factory = RequestFactory()


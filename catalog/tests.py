from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from catalog.views import index

class CatalogHomePageTest(TestCase):

    def test_POST_request_saved(self):
        response = self.client.post('/',  data={'plant_entry': 'A new plant'})
        assert 'A new plant' in response.content.decode()
        self.assertTemplateUsed(response, 'home.html')
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from catalog.views import index
from catalog.models import Plant


class CatalogHomePageTest(TestCase):

    def test_POST_request_saved(self):
        response = self.client.post('/',  data={'plant_entry': 'A new plant'})
        assert 'A new plant' in response.content.decode()
        self.assertTemplateUsed(response, 'home.html')


class CatalogModelTest(TestCase):

    def test_plants_saved(self):
        first_plant = Plant()
        first_plant.name = 'Scindapsus pictus'
        first_plant.save()

        second_plant = Plant()
        second_plant.name = 'Philodendron micans'
        second_plant.save()

        saved_items = Plant.objects.all()

        assert saved_items.count() == 2

        first_saved_plant = saved_items[0]
        second_saved_plant = saved_items[1]

        assert first_saved_plant.name == 'Scindapsus pictus'
        assert second_saved_plant.name == 'Philodendron micans'
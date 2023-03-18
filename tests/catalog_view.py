import pytest
from pytest_django.asserts import assertTemplateUsed

from django.test import Client 

from catalog.views import home_page
from catalog.models import Plant


class HomePageTest(Client):
    '''Test class for web-app home page.'''

    def test_home_template_used(self):
        '''
        Make sure the correct template is served to the client when
        they navigate to the root website url.
        '''
        response = self.get('/')
        assertTemplateUsed(response, 'home.html')


    def test_POST_request_saved(self):
        '''
        Make sure the POST request submitted by the client is saved to the
        server using Django's ORM
        '''
        self.post('/', data={'plant_entry': 'A new plant'})
        assert Plant.objects.count() == 1 
        new_plant = Plant.objects.first()  
        assert new_plant.name == 'A new plant'


    def test_redirected_after_POST(self):
        ''' 
        Make sure the client is redirected after submitting
        a POST request to the server.
        '''
        response = self.post('/', data={'plant_entry': 'A new plant'})
        assert response.status_code == 302
        assert response['location'] == '/'


    def test_only_necessary_requests_saved(self):
        '''
        Make sure only submitted plant entries are saved.
        '''
        self.get('/')
        assert Plant.objects.count() == 0


    def test_all_plants_displayed(self):
        '''
        Make sure the user is able to see all of their plants at once.
        '''
        Plant.objects.create(name='SomePlant1')
        Plant.objects.create(name='SomePlant2')

        response = self.get('/')

        assert 'SomePlant1' in response.content.decode()
        assert 'SomePlant2' in response.content.decode()


class PlantModelTest():
    ''' Test class for Plant model.'''

    def test_plants_saved_and_received(self):
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
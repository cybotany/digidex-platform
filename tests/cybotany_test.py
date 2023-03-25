import pytest
from pytest_django.asserts import assertTemplateUsed

from catalog.views import home_page
from catalog.models import Plant

class TestCatalogView():
    '''
    Test class for web-app home page.
    client is a fixture provided by the pytest-django plugin
    '''

    @pytest.mark.django_db
    def test_home_template_used(self, client):
        '''
        Make sure the correct template is served to the client when
        they navigate to the root website url.
        '''
        response = client.get('/')
        assertTemplateUsed(response, 'home.html')


    @pytest.mark.django_db
    def test_POST_request_saved(self, client):
        '''
        Make sure the POST request submitted by the client is saved to the
        server using Django's ORM
        '''
        client.post('/', data={'plant_entry': 'A new plant'})
        assert Plant.objects.count() == 1 
        new_plant = Plant.objects.first()  
        assert new_plant.name == 'A new plant'


    @pytest.mark.django_db
    def test_redirected_after_POST(self, client):
        ''' 
        Make sure the client is redirected after submitting
        a POST request to the server.
        '''
        response = client.post('/', data={'plant_entry': 'A new plant'})
        assert response.status_code == 302
        assert response['location'] == '/'


    @pytest.mark.django_db
    def test_only_necessary_requests_saved(self, client):
        '''
        Make sure only submitted plant entries are saved.
        '''
        client.get('/')
        assert Plant.objects.count() == 0


    @pytest.mark.django_db
    def test_all_plants_displayed(self, client):
        '''
        Make sure the user is able to see all of their plants at once.
        '''
        Plant.objects.create(name='SomePlant1')
        Plant.objects.create(name='SomePlant2')

        response = client.get('/')

        assert 'SomePlant1' in response.content.decode()
        assert 'SomePlant2' in response.content.decode()


class TestPlantModel():
    ''' Test class for Plant model.'''

    @pytest.mark.django_db
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
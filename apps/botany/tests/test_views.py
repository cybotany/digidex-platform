from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class PlantHomepageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.url = reverse('botany:home')

    def test_plant_homepage_view_contains_two_containers(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get(self.url)

        # Check if the response contains the left container
        self.assertContains(response, '<div id="left-container">', html=True)

        # Check if the response contains the right container
        self.assertContains(response, '<div id="right-container">', html=True)

        # Check if the right container contains the four boxes
        self.assertContains(response, '<div class="box" id="register-label">', html=True)
        self.assertContains(response, '<div class="box" id="register-medium">', html=True)
        self.assertContains(response, '<div class="box" id="register-fertilizer">', html=True)

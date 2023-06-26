from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.db import IntegrityError

from apps.botany.models import Label, Plant, PlantImage

User = get_user_model()


class LabelModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.label1 = Label.objects.create(name='Label 1', user=self.user)
        self.label2 = Label.objects.create(name='Label 2', user=self.user)
        self.common_label = Label.objects.create(name='Common Label', is_common=True)

    def test_label_str(self):
        self.assertEqual(str(self.label1), 'Label 1')

    def test_label_unique_together(self):
        with self.assertRaises(Exception):
            Label.objects.create(name='Label 1', user=self.user)

    def test_get_common_labels(self):
        common_labels = Label.get_common_labels()
        self.assertEqual(len(common_labels), 1)
        self.assertEqual(common_labels[0], self.common_label)

    def test_label_plants(self):
        plant1 = Plant.objects.create(name='Plant 1', description='Description 1', owner=self.user, label=self.label1)
        plant2 = Plant.objects.create(name='Plant 2', description='Description 2', owner=self.user, label=self.label1)
        self.assertEqual(list(self.label1.plants), [plant1, plant2])
        self.assertNotEqual(list(self.label2.plants), [plant1, plant2])


class PlantModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.label = Label.objects.create(name='Test Label', user=self.user)

    def test_create_plant(self):
        plant = Plant.objects.create(
            name="Test Plant",
            label=self.label,
            owner=self.user,
            description="This is a test plant"
        )
        self.assertEqual(plant.name, "Test Plant")
        self.assertEqual(plant.owner, self.user)
        self.assertEqual(plant.label, self.label)
        self.assertIsNotNone(plant.added_on)

    def test_create_plant_without_name(self):
        plant = Plant.objects.create(
            label=self.label,
            owner=self.user,
            description="This is a test plant without a name"
        )
        self.assertEqual(plant.name, "Plant-1")
        self.assertEqual(plant.owner, self.user)
        self.assertEqual(plant.label, self.label)
        self.assertIsNotNone(plant.added_on)

    def test_get_absolute_url(self):
        plant = Plant.objects.create(
            name="Test Plant",
            label=self.label,
            owner=self.user,
            description="This is a test plant"
        )
        expected_url = reverse('botany:describe_plant', args=[str(plant.id)])
        self.assertEqual(plant.get_absolute_url(), expected_url)


class PlantImageModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.plant = Plant.objects.create(name='Test Plant', owner=self.user)

    def test_create_plant_image(self):
        # Create an in-memory image file for testing
        image = SimpleUploadedFile(
            name='test_plant.jpg',
            content=open('static/img/test-plant.jpg', 'rb').read(),
            content_type='image/jpeg'
        )
        plant_image = PlantImage.objects.create(plant=self.plant, image=image)
        self.assertEqual(plant_image.plant, self.plant)
        self.assertIsNotNone(plant_image.uploaded_at)

    def test_missing_plant_raises_error(self):
        with self.assertRaises(IntegrityError):
            PlantImage.objects.create(image='image.jpg')

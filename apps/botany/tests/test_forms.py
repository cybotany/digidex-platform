from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.db.models import Q

from apps.botany.models import Plant, Label, PlantImage
from apps.botany.forms import PlantLabelForm, PlantRegistrationForm, PlantUpdateForm

User = get_user_model()


class PlantLabelFormTest(TestCase):

    def test_valid_data(self):
        form = PlantLabelForm({'name': 'Fern'})
        self.assertTrue(form.is_valid())

    def test_missing_name(self):
        form = PlantLabelForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['Please provide a label name.'])

    def test_max_length_exceeded(self):
        name = 'a' * 101  # 101 characters
        form = PlantLabelForm({'name': name})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['name'], ['Label name should not exceed 100 characters.'])


class PlantRegistrationFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.common_label = Label.objects.create(name='Common', is_common=True)
        self.user_label = Label.objects.create(name='Personal', user=self.user)

    def test_without_image(self):
        form = PlantRegistrationForm(
            data={'name': 'Tulip', 'label': self.user_label.id, 'description': 'A colorful tulip'},
            user=self.user
        )
        self.assertTrue(form.is_valid())
        plant = form.save()
        self.assertEqual(PlantImage.objects.filter(plant=plant).count(), 0)

    def test_label_queryset(self):
        form = PlantRegistrationForm(user=self.user)
        self.assertQuerysetEqual(
            form.fields['label'].queryset.order_by('name'),
            Label.objects.filter(Q(user=self.user)).order_by('name'),
            transform=lambda x: x
        )


class PlantUpdateFormTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.plant = Plant.objects.create(name='Rose', description='A red rose', user=self.user)

    def test_update_without_image(self):
        form = PlantUpdateForm(
            instance=self.plant,
            data={'name': 'Updated Rose', 'description': 'An updated red rose'}
        )
        self.assertTrue(form.is_valid())
        updated_plant = form.save()
        self.assertEqual(PlantImage.objects.filter(plant=updated_plant).count(), 0)

    def test_update_with_existing_image(self):
        image = SimpleUploadedFile(name='test_image.jpg', content=b'image content', content_type='image/jpeg')
        PlantImage.objects.create(plant=self.plant, image=image)

        form = PlantUpdateForm(
            instance=self.plant,
            data={'name': 'Updated Rose Again', 'description': 'Another updated red rose'}
        )
        self.assertTrue(form.is_valid())
        updated_plant = form.save()
        self.assertEqual(updated_plant.name, 'Updated Rose Again')
        self.assertEqual(PlantImage.objects.filter(plant=updated_plant).count(), 1)

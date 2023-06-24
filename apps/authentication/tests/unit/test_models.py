from django.contrib.auth import get_user_model
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from apps.authentication.models import Profile


class ProfileModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            bio="This is a test bio.",
            location="Test City",
            birth_date="1990-01-01",
            avatar=SimpleUploadedFile(
                name='test_avatar.jpg',
                content=b'simple_file_content',
                content_type='image/jpeg'
            )
        )

    def test_profile_creation(self):
        self.assertEqual(self.profile.user.username, 'testuser')
        self.assertEqual(self.profile.bio, 'This is a test bio.')
        self.assertEqual(self.profile.location, 'Test City')
        self.assertEqual(str(self.profile.birth_date), '1990-01-01')
        self.assertIsNotNone(self.profile.avatar)

    def test_profile_string_representation(self):
        self.assertEqual(str(self.profile), "testuser's Profile")

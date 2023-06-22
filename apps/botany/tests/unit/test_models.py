from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.botany.models import Label

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

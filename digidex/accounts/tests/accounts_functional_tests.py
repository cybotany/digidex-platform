import pytest
from django.test import TestCase
from wagtail.test.utils import WagtailPageTestCase


@pytest.mark.usefixtures("browser")
class TestNewVisitor:
    def test_can_start_a_todo_list(self, browser):
        # Edith has heard about a cool new online to-do app.
        # She goes to check out its homepage
        browser.get("http://localhost:8000")

        # She notices the page title and header mention to-do lists
        assert "DigiDex" in browser.title

        # She is invited to enter a to-do item straight away
        pytest.fail("Finish the test!")

        # Satisfied, she goes back to sleep


class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1 + 1, 3)

import pytest
from django.core.exceptions import ValidationError
from wagtail.test.utils import WagtailPageTestCase

from home.models import HomePage


class TestHomePageFields(WagtailPageTestCase):

    def test_hero_heading_max_length(self):
        home_page = HomePage(hero_heading='x' * 256)  # 256 characters
        with pytest.raises(ValidationError):
            home_page.full_clean()

    def test_hero_paragraph_blank(self, home_page):
        home_page.hero_paragraph = ""
        try:
            home_page.full_clean()
            assert True  # Should not raise an error
        except ValidationError:
            assert False

class TestHomePageMethods(WagtailPageTestCase):

    def test_create_user_profile_index_page_no_existing(self, home_page):
        profile_page = home_page.create_user_profile_index_page()
        assert profile_page.title == "Users"
        assert home_page.get_children().count() == 1

    def test_create_user_profile_index_page_existing(self, home_page, user_profile_index_page):
        # Assuming user_profile_index_page is already created as a child of home_page
        profile_page = home_page.create_user_profile_index_page()
        assert profile_page == user_profile_index_page
        assert home_page.get_children().count() == 1  # No additional page should be created

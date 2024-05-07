import pytest
from django.test import Client
from wagtail.models import Page

from home.models import HomePage, UserProfileIndexPage
from accounts.models import User


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def new_user(db):
    return User.objects.create_user(username='testuser', password='testpass123')


@pytest.fixture
def home_page():
    root_page = Page.objects.get(id=1)
    home_page = HomePage(title="Home", slug="home")
    root_page.add_child(instance=home_page)
    return home_page

@pytest.fixture
def user_profile_index_page():
    home_page = HomePage.objects.get(slug="home")
    user_profile_index_page = UserProfileIndexPage(
        title="Users", heading="Welcome", intro="Profiles Intro", slug="u")
    home_page.add_child(instance=user_profile_index_page)
    return user_profile_index_page

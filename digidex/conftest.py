import pytest
from wagtail.models import Page

from inventory.models.landing import HomePage
from accounts.models import User
from selenium import webdriver


@pytest.fixture(scope="class")
def browser():
    # Set up the browser once for all tests in this class
    driver = webdriver.Firefox()
    yield driver
    # Quit the browser after all tests have run
    driver.quit()


@pytest.fixture
def home_page():
    root_page = Page.objects.get(id=1)
    home_page = HomePage(title="Home", slug="home")
    root_page.add_child(instance=home_page)
    return home_page


@pytest.fixture
def new_user(db):
    return User.objects.create_user(username='testuser', password='testpass123')

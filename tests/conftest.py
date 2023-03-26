# conftest.py
'''
Just some custom fixtures to use in other tests.
'''
from decouple import config
from selenium import webdriver
import pytest


@pytest.fixture(scope='class')
def ff_driver(request):
    driver = webdriver.Firefox()
    request.cls.browser = driver
    yield driver
    driver.quit()


@pytest.fixture
def website_url():
    return config("WEBSITE_URL")

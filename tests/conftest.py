# conftest.py
'''
Just some custom fixtures to use in other tests.
'''
from decouple import config
from selenium import webdriver
import pytest


@pytest.fixture
def ff_driver():
    return webdriver.Firefox()

@pytest.fixture
def website_url():
    return config("WEBSITE_URL")

from selenium import webdriver
import pytest

browser = webdriver.Firefox()

class Plant:
    def __init__(self, name):
        self.name = name

# User navigates to the homepage of the eukix-app
browser.get('http://localhost:8000')

# User notices the page title and header mention Django
assert 'Django' in browser.title

# User is prompted to 
from selenium import webdriver
import pytest

browser = webdriver.Firefox()

class Customer:
    def __init__(self, name):
        self.name = name

# User navigates to the homepage of the rotomi-app
browser.get('http://localhost:8000')

# User notices the page title and header mention rotomi
assert 'Django' in browser.title

# User is prompted to login
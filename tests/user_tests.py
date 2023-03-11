from selenium import webdriver
import pytest

browser = webdriver.Firefox()

class Plant:
    def __init__(self, plant_id, tax_id):
        self.id = id

# User scans plant container which directs them to the app.
browser.get('http://localhost:8000/plant')

# User is prompted to create an account or log-in.

# User logs in to their account and is redirected to the plant registration view

# User is prompted to fill in values regarding plant with UID automatically generated


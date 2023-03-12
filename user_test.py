from selenium import webdriver
import pytest

browser = webdriver.Firefox()

# User scans NFC tag which directs them to the web-app
browser.get('http://localhost:8000/main')

# Application checks cache to see if user log in necessary

# User is prompted to create an account if no cache data is found

# User creates their account and is redirected to the tag registration view

# Check if this tag is already registered to a user

# If tag is not registered to another user, prompt user to register it

# Tag registration automatically pull tag metadata from the NFC reader

# Tag registration will map tag to 1 user at any given time

# Tag registration will map tag to 1 plant at any given time

# Tag registration will map tag to 1 location at any given time

# Tag registration will map tag to 1 or 0 CEA greenhouse (Controlled Environment Agriculture) at any given time

# Tag will ask user if they would like to create a care schedule after cataloging their plant

# Tag will ask user if they would like to design an experiment after cataloging their plant 

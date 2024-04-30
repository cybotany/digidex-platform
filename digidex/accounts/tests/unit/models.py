import pytest
from django.contrib.auth.models import Group
from accounts.models import User, UserProfile

@pytest.mark.django_db
def test_create_user_group():
    # Create a user
    user = User.objects.create(username='testuser', email='testuser@example.com')
    
    # Test create_user_group method
    group, created = user.create_user_group()

    # Asserts
    assert created is True
    assert group.name == f"user_{user.username}_group"
    assert group in user.groups.all()

@pytest.mark.django_db
def test_create_user_profile():
    # Create a user
    user = User.objects.create(username='testuser', email='testuser@example.com')
    
    # Test create_user_profile method
    profile, created = user.create_user_profile()

    # Asserts
    assert created is True
    assert profile.user == user

    # Check if UserProfile is saved properly
    assert UserProfile.objects.filter(user=user).exists()

from django.core.management.base import BaseCommand

from wagtail.models import Site

from accounts.models import UserProfileIndexPage, UserProfilePage, UserProfile

class Command(BaseCommand):
    help = 'Creates user profile pages for all users'

import logging
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_save, post_migrate
from django.dispatch import receiver
from wagtail.models import Site

from accounts.models import User, UserProfile, UserProfileIndexPage, UserProfilePage

logger = logging.getLogger(__name__)


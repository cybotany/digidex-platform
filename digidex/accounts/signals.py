from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from wagtail.models import Collection

from accounts.models import User

@receiver(post_save, sender=User)
def create_user_assets(sender, instance, created, **kwargs):
    if created:
        with transaction.atomic():
            _profile, _profile_created  = instance.create_user_profile()

            accounts_collection = Collection.objects.filter(name="Accounts").first()
            if accounts_collection is None:
                root_collection = Collection.get_first_root_node()
                accounts_collection = root_collection.add_child(name="Accounts")

            if _profile_created:
                _collection = _profile.create_user_collection(parent=accounts_collection)
                _url = _profile.create_user_profile_page() 

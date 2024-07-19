from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from inventory.models import Inventory
from category.models import Category

@receiver(post_save, sender=Inventory)
def create_user_party_category(sender, instance, created, **kwargs):
    if created:
        name = "Party"

        parent_collection = instance.collection
        category_collection = parent_collection.add_child(name=name)

        category = Category(
            title=name,
            name=name,
            slug=slugify(name),
            owner=instance.owner,
            collection=category_collection
        )
        instance.add_child(instance=category)

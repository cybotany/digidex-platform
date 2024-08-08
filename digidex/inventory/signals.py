from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from inventory.models import InventoryIndexPage, TrainerInventoryPage, NearFieldCommunicationTag


User = get_user_model()

@receiver(post_save, sender=User)
def new_user_setup(sender, instance, created, **kwargs):
    if created:
        inventory_index = InventoryIndexPage.objects.first()
        trainer_inventory_page = TrainerInventoryPage(
            title=instance.username.title(),
            slug=slugify(instance.username),
            owner=instance
        )
        inventory_index.add_child(instance=trainer_inventory_page)
        trainer_inventory_page.save_revision().publish()

@receiver(post_save, sender=NearFieldCommunicationTag)
def create_inventory_link(sender, instance, created, **kwargs):
    if created:
        instance.create_link()

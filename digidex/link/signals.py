from django.db.models.signals import post_save
from django.dispatch import receiver
from digidex.inventory.models import Plant, Pet
from digidex.journal.models import Collection

@receiver(post_save, sender=Plant)
def create_journal_collection_for_plant(sender, instance, created, **kwargs):
    """
    Create a Journal Collection for every new Plant instance.
    """
    if created:
        Collection.objects.create(plant=instance)

@receiver(post_save, sender=Pet)
def create_journal_collection_for_pet(sender, instance, created, **kwargs):
    """
    Create a Journal Collection for every new Pet instance.
    """
    if created:
        Collection.objects.create(pet=instance)

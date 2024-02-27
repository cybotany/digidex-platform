from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from digidex.inventory.models import Plant, Pet
from digidex.journal.models import Collection

def create_journal_collection(instance, **kwargs):
    """
    Create a Journal Collection for a new Digit instance.
    This function is generalized to work with any model instance.
    """
    Collection.objects.create(
        content_type=ContentType.objects.get_for_model(instance.__class__),
        object_id=instance.id
    )

@receiver(post_save, sender=Plant)
def create_journal_collection_for_plant(sender, instance, created, **kwargs):
    """
    Signal to create a Journal Collection for every new Plant instance.
    """
    if created:
        create_journal_collection(instance, **kwargs)

@receiver(post_save, sender=Pet)
def create_journal_collection_for_pet(sender, instance, created, **kwargs):
    """
    Signal to create a Journal Collection for every new Pet instance.
    """
    if created:
        create_journal_collection(instance, **kwargs)

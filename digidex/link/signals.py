from django.db.models.signals import post_save
from django.dispatch import receiver
from digidex.inventory.models import Digit
from digidex.journal.models import Collection

@receiver(post_save, sender=Digit)
def create_journal_collection_for_digit(sender, instance, created, **kwargs):
    """
    Create a Journal Collection for every new Digit instance.
    """
    if created:  # Check if it's a new instance
        Collection.objects.create(digit=instance)

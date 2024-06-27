from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import TrainerPage
from .utils import create_trainer_collection


@receiver(post_save, sender=TrainerPage)
def create_trainer_collection(sender, instance, created, **kwargs):
    if created:
        trainer_collection = create_trainer_collection(instance.owner)
        instance.collection = trainer_collection
        instance.save()

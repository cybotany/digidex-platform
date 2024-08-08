from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.text import slugify

from inventory.models import InventoryIndexPage, TrainerInventoryPage, NearFieldCommunicationTag


User = get_user_model()

@receiver(post_save, sender=User)
def new_user_setup(sender, instance, created, **kwargs):
    if created:
        # Create trainer inventory page as a child of the inventory index page
        inventory_index = InventoryIndexPage.objects.first()
        trainer_inventory_page = TrainerInventoryPage(
            title=instance.username.title(),
            slug=slugify(instance.username),
            owner=instance,
            trainer=instance
        )
        inventory_index.add_child(instance=trainer_inventory_page)
        trainer_inventory_page.save_revision().publish()

        # Create a group for the trainer
        trainer_uuid = instance.uuid
        trainer_group = Group.objects.create(name=str(trainer_uuid))

        # Assign page permissions to the group
        permissions = Permission.objects.filter(
            codename__in=[
                'add_trainerinventorypage',
                'change_trainerinventorypage',
                'delete_trainerinventorypage',
                'publish_trainerinventorypage'
            ]
        )
        for permission in permissions:
            trainer_group.permissions.add(permission)

        # Assign document and image permissions to the group
        permissions = Permission.objects.filter(
            codename__in=[
                'add_document',
                'change_document',
                'choose_document',
                'add_image',
                'change_image',
                'choose_image'
            ]
        )
        for permission in permissions:
            trainer_group.permissions.add(permission)

        # Assign collection management permissions to the group
        permissions = Permission.objects.filter(
            codename__in=[
                'add_collection',
                'change_collection',
                'delete_collection'
            ]
        )
        for permission in permissions:
            trainer_group.permissions.add(permission)

        # Assign the trainer to their group
        instance.groups.add(trainer_group)


@receiver(post_save, sender=NearFieldCommunicationTag)
def create_inventory_link(sender, instance, created, **kwargs):
    if created:
        instance.create_link()

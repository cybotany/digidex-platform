from django.db.models.signals import post_save
from django.dispatch import receiver
from inventory.models import UserDigitizedObject

@receiver(post_save, sender=UserDigitizedObject)
def create_user_digit_page(sender, instance, created, **kwargs):
    if created:
        instance.create_digit_page()

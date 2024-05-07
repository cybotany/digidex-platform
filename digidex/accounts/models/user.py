import uuid
from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from wagtail.models import Collection


class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="User UUID"
    )

    def build_root_user_collection(self):
        return Collection.objects.get_or_create(
                name='Users',
                defaults={'depth': 1}
            )

    def build_user_collection_name(self):
        return f"{self.username}'s Collection"

    def check_for_existing_collection(self, collection_name, root_collection):
        """
        Method to check if a user collection already exists for the associated user.
        """
        return Collection.objects.filter(
                name=collection_name, 
                depth=root_collection.depth + 1, 
                path__startswith=root_collection.path
            ).first()

    def create_user_collection(self):
        """
        Method to create or retrieve a user collection for the associated user.
        """
        with transaction.atomic():
            # Ensure the 'Users' root collection exists
            users_root_collection, _ = self.build_root_user_collection()
            # Define the name for the specific user's collection
            user_collection_name = self.build_user_collection_name()
            # Check if a collection with this name already exists under 'Users'
            user_collection = self.check_for_existing_collection(user_collection_name, users_root_collection)
            # If the collection does not exist, create it as a child of 'Users'
            if not user_collection:
                user_collection = users_root_collection.add_child(
                    name=user_collection_name
                )
            # Link user to the new collection
            user_collection_link, created = UserCollection.objects.get_or_create(
                user=self,
                collection=user_collection
            )
            return user_collection_link


class UserCollection(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='user_collection'
    )
    collection = models.OneToOneField(
        Collection,
        on_delete=models.CASCADE,
        related_name='owner'
    )


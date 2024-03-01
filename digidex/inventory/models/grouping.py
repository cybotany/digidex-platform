from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class Grouping(models.Model):
    """
    Model for organizing digitized entities into groups.

    Attributes:
        name (CharField): A human-readable name for the digitized grouping entity.
        slug (SlugField): A short label for the digitized grouping entity.
        description (TextField): A short description of the digitized grouping entity.
        user (ForeignKey): A relationship to the User model.
        is_default (BooleanField): Indicates if this is the default grouping for the user. Default groupings cannot be deleted.
        created_at (DateTimeField): The date and time when the Grouping instance was created.
        last_modified (DateTimeField): The date and time when the Grouping instance was last modified.
    """
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        help_text="The name of the group."
    )
    slug = models.SlugField(
        max_length=255,
        blank=True,
        db_index=True,
        help_text="The slug for the group."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="The description of the group."
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='digit_groups',
        on_delete=models.CASCADE,
        help_text="A relationship to the User model."
    )
    is_default = models.BooleanField(
        default=False,
        help_text="Indicates if this is the default grouping for the user. Default groupings cannot be deleted."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the grouping instance was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the grouping instance was last modified."
    )
    class Meta:
        unique_together = ('user', 'name')

    def __str__(self):
        return self.name

    def _get_items(self, item_type):
        """
        Private method to retrieve or count items (plants or pets).
        
        Parameters:
        - item_type (str): Type of items to retrieve ('plants' or 'pets').
        """
        return getattr(self, item_type)

    def _get_user_plants(self):
        return self._get_items('plants')

    def _get_user_pets(self):
        return self._get_items('pets')

    def _get_parent_url(self):
        """
        Returns the URL of the parent object.
        """
        return reverse('inventory:detail-profile', kwargs={'user_slug': self.user.slug})

    def _get_parent_name(self):
        """
        Returns the name of the parent object.
        """
        return self.user.username

    @property
    def is_public(self):
        """
        Property to check if the grouping is public based on the user's profile setting.
        """
        return self.user.profile.is_public

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        original_slug = self.slug
        num = 1
        while Grouping.objects.filter(user=self.user, slug=self.slug).exclude(pk=self.pk).exists():
            self.slug = f"{original_slug}-{num}"
            num += 1
        super(Grouping, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if not self.is_default:
            super(Grouping, self).delete(*args, **kwargs)
        else:
            pass

    def get_absolute_url(self):
        """
        Returns the absolute URL to the Grouping's detail page.
        """
        if self.is_default:
            return reverse('inventory:detail-profile', kwargs={'user_slug': self.user.slug})
        return reverse('inventory:detail-grouping', kwargs={'user_slug': self.user.slug, 'group_slug': self.slug})

    def get_digits(self, digit_type='all'):
        """
        Returns QuerySets of plants, pets, or both for this grouping, along with their counts, 
        based on ownership status and digit type.
        
        Parameters:
        - digit_type (str): Specifies the digit type to return ('plants', 'pets', or 'all').

        Returns:
        A dictionary with the items and their counts for plants and/or pets.
        """
        digits = {}
        if digit_type in ['plants', 'pets', 'all']:
            if digit_type in ['plants', 'all']:
                plants = self._get_user_plants().all()
                digits['plants'] = {
                    'items': plants,
                    'count': plants.count()
                }
            if digit_type in ['pets', 'all']:
                pets = self._get_user_pets().all()
                digits['pets'] = {
                    'items': pets,
                    'count': pets.count()
                }
        return digits

    def get_details(self):
        """
        Returns information about the grouping, including the URL and its name 
        
        Returns:
        A dictionary containing the 'url' and 'name' of the grouping.
        """
        return {
            'url': self.get_absolute_url(),
            'name': self.name
        }

    def get_parent_details(self):
        """
        Returns information about the grouping's owner, including the URL to their profile 
        and their username.
        
        Returns:
        A dictionary containing the 'url' and 'name' of the grouping's owner.
        """
        return {
            'url': self._get_parent_url(),
            'name': self._get_parent_name()
        }

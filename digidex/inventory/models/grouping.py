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

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # Ensure the slug is unique for the user
        original_slug = self.slug
        num = 1
        # Check for existing slugs that are the same and append a number to make the new slug unique
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
        return reverse('inventory:detail-grouping', kwargs={'user_slug': self.user.slug, 'group_slug': self.slug})

    def _get_items(self, item_type, is_owner):
        """
        Private method to retrieve or count items (plants or pets) based on ownership.
        
        Parameters:
        - item_type (str): Type of items to retrieve ('plants' or 'pets').
        - is_owner (bool): Ownership status to filter items.
        """
        items = getattr(self, item_type)
        if not is_owner:
            items = items.filter(is_public=False)
        return items

    def _get_user_plants(self, is_owner=False):
        return self._get_items('plants', is_owner)

    def _count_user_plants(self, is_owner=False):
        return self._get_items('plants', is_owner).count()

    def _get_user_pets(self, is_owner=False):
        return self._get_items('pets', is_owner)

    def _count_user_pets(self, is_owner=False):
        return self._get_items('pets', is_owner).count()

    def get_counts(self, is_owner=False, digit_type='all'):
        """
        Returns counts of plants, pets, or both for this grouping, based on ownership status and digit type.

        Parameters:
        - is_owner (bool): Determines whether to count all items or only those that are not public.
        - digit_type (str): Specifies the digit type to return ('plants', 'pets', or 'all').
        
        Returns:
        A dictionary with counts for plants and pets.
        """
        counts = {}
        if digit_type in ['plants', 'all']:
            counts['plant_count'] = self._count_user_plants(is_owner)
        if digit_type in ['pets', 'all']:
            counts['pet_count'] = self._count_user_pets(is_owner)
        return counts

    def get_digits(self, is_owner=False, digit_type='all'):
        """
        Returns QuerySets of plants, pets, or both for this grouping, based on ownership status and digit type.
        
        Parameters:
        - is_owner (bool): Determines whether to count all items or only those that are not public.
        - digit_type (str): Specifies the digit type to return ('plants', 'pets', or 'all').

        Returns:
        A dictionary with counts for plants and pets.
        """
        digits = {}
        if digit_type in ['plants', 'all']:
            digits['plants'] = self._get_user_plants(is_owner).all()
        if digit_type in ['pets', 'all']:
            digits['pets'] = self._get_user_pets(is_owner).all()
        return digits

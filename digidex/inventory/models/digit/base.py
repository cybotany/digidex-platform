import uuid
from django.urls import reverse
from django.db import models, transaction
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ObjectDoesNotExist

from digidex.journal.models import collection as journal_collection
from digidex.journal.models import entry as journal_entry
from digidex.inventory.models import grouping as digit_grouping
from digidex.taxonomy.models.itis.taxon import base as base_taxon
from digidex.taxonomy.models.itis.taxon import kingdom as base_kingdom
from digidex.taxonomy.models.itis.taxon import rank as base_rank

class Digit(models.Model):
    """
    Abstract base model for digitized entities, serving as a bridge between physical specimens and their digital representations.

    Attributes:
        uuid (UUIDField): The unique identifier associated with each Digit.
        name (CharField): A human-readable name for the digitized entity.
        description (TextField): A short description of the digitized entity.
        grouping (ForeignKey): The grouping this digit belongs to.

        
        taxon (ForeignKey): A relationship to the Unit model, representing the entity's taxonomic classification.
        ntag (OneToOneField): A relationship to the Link model, representing the NTAG link for the digitized entity.
        is_public (BooleanField): Indicates if the digit should be publicly visible to the public or private. Digit is private by default.
        is_archived (BooleanField): Indicates whether the digit is archived.
        created_at (DateTimeField): The date and time when the Digit instance was created.
        last_modified (DateTimeField): The date and time when the Digit instance was last modified.
    """
    _itis_kingdom_pk = None
    _itis_rank_pk = None
    _itis_taxon_pk = None

    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digit UUID",
        help_text="The unique identifier associated with the Digit."
    )
    name = models.CharField(
        max_length=50,
        null=True,
        blank=True,
        help_text="A human-readable name for the digitized entity."
    )
    description = models.TextField(
        max_length=500,
        null=True,
        blank=True,
        help_text="A short description of the digitized entity."
    )
    grouping = models.ForeignKey(
        'inventory.Grouping',
        on_delete=models.CASCADE,
        related_name="%(class)ss", # The second "s" at the end is intentional
        help_text="The grouping this digit belongs to."
    )
    ntag = models.OneToOneField(
        'link.NTAG',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='%(class)s',
        help_text="NTAG link for the digitized entity."
    )
    is_public = models.BooleanField(
        default=False,
        help_text='Indicates if the digit should be publicly visible to the public or private. Digit is private by default.'
    )
    # Taxonomy fields
    kingdom = models.ForeignKey(
        'taxonomy.ItisTaxonKingdom',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        help_text="The taxonomic kingdom of the digitized entity."
    )
    rank = models.ForeignKey(
        'taxonomy.ItisTaxonRank',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(class)ss", # The second "s" at the end is intentional
        help_text="The taxonomic rank of the digitized entity."
    )
    taxon = models.ForeignKey(
        'taxonomy.ItisTaxonUnit',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="%(class)ss", # The second "s" at the end is intentional
        help_text="The taxonomic classification of the digitized entity."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created At",
        help_text="The date and time when the digit instance was created."
    )
    last_modified = models.DateTimeField(
        auto_now=True,
        verbose_name="Last Modified",
        help_text="The date and time when the digit instance was last modified."
    )

    def _get_itis_kingdom_pk(self):
        """
        Retrieves the Primary Key used for the ITIS taxonomic kingdom database tabel.
        This method is intended to be overridden by subclasses.
        """
        return self._itis_kingdom_pk

    def _get_itis_rank_pk(self):
        """
        Retrieves the Primary Key used for the ITIS taxonomic rank database tabel.
        This method is intended to be overridden by subclasses.
        """
        return self._itis_rank_pk

    def _get_itis_taxon_pk(self):
        """
        Retrieves the Primary Key used for the ITIS taxonomic unit database tabel.
        This method is intended to be overridden by subclasses.
        """
        return self._itis_taxon_pk

    def get_digit_type(self):
        return self.__class__.__name__.lower()

    def save(self, *args, **kwargs):
        """
        Overrides the save method of the model. If name is not provided, it sets a default name 
        based on the count of Digits the user has.
        """
        if not self.grouping_id:
            default_grouping, _ = digit_grouping.Grouping.objects.get_or_create(
                user=self.ntag.user,
                is_default=True,
                defaults={
                    'name': 'Default Grouping',
                    'description': 'This is an automatically created default grouping.'
                }
            )
            self.grouping = default_grouping

        if not self.kingdom:
            self.kingdom = self.get_kingdom()  

        if not self.rank:
            self.rank = self.get_rank()  

        if not self.taxon:
            self.taxon = self.get_taxon()        

        if not self.name:
            self.name = "Digit"

        super().save(*args, **kwargs)

    @classmethod
    def create_digit(cls, form_data, link, user):
        with transaction.atomic():    
            digit = cls.objects.create(
                ntag=link,
                **form_data
            )
            link.user = user
            link.active = True
            link.save()

            return digit

    def delete(self, *args, **kwargs):
        """
        Overrides the delete method of the model to include custom deletion logic.
        """
        # Reset the NTAG link to default and save it
        if self.ntag:
            self.ntag.reset_to_default()
            self.ntag.save()
        super(Digit, self).delete(*args, **kwargs)

    def get_absolute_url(self):
        """
        Get the URL to view the details of this digitized entity, using query parameters.
        """
        ntag_use = self.ntag.get_use()
        if ntag_use == 'plant':
            _type = 'plant'
        else:
            _type = 'pet'
        return reverse('inventory:detail-digit', kwargs={'type': _type, 'uuid': self.uuid})

    @classmethod
    def get_kingdom(cls):
        itis_kingdom_pk = cls()._get_itis_kingdom_pk()
        if itis_kingdom_pk:
            try:
                return base_kingdom.ItisTaxonKingdom.objects.get(pk=itis_kingdom_pk)
            except ObjectDoesNotExist:
                raise ValueError(f"Taxon Kingdom with the primary key {itis_kingdom_pk} does not exist in the ITIS database.")
        else:
            raise NotImplementedError("This method must be implemented by subclasses.")

    @classmethod
    def get_rank(cls):
        itis_rank_pk = cls()._get_itis_taxon_pk()
        if itis_rank_pk:
            try:
                return base_rank.ItisTaxonRank.objects.get(pk=itis_rank_pk)
            except ObjectDoesNotExist:
                raise ValueError(f"Taxon Rank with the primary key {itis_rank_pk} does not exist does not exist in the ITIS database.")
        else:
            raise NotImplementedError("This method must be implemented by subclasses.")

    @classmethod
    def get_taxon(cls):
        """
        Retrieves the taxon using the ITIS taxonomic serial number.
        """
        itis_taxon_pk = cls()._get_itis_taxon_pk()
        if itis_taxon_pk:
            try:
                return base_taxon.ItisTaxonUnit.objects.get(pk=itis_taxon_pk)
            except ObjectDoesNotExist:
                raise ValueError(f"Taxon with the serial number {itis_taxon_pk} does not exist does not exist in the ITIS database.")
        else:
            raise ValueError("ITIS Taxon PK not defined.")

    def get_journal_entries(self):
        """
        Fetches all Entry objects related to this Digit instance through its Collection.
        Returns a QuerySet of Entry instances.
        """
        content_type = ContentType.objects.get_for_model(self.__class__)
        collections = journal_collection.Collection.objects.filter(content_type=content_type, object_id=self.pk)

        if collections.exists():
            collection = collections.first()
            entries = collection.get_all_entries()
            return entries
        return journal_entry.Entry.objects.none()

    def get_parent_details(self):
        """
        Returns information about the grouping's owner, including the URL to their profile 
        and their username.
        
        Returns:
        A dictionary containing the 'url' and 'name' of the grouping's owner.
        """
        if self.grouping.is_default:
            return self.grouping.get_parent_details()
        return self.grouping.get_details()

    class Meta:
        abstract = True
        ordering = ['-created_at']
        
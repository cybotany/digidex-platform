from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType


class CEA(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class GrowthChamber(CEA):
    MEASUREMENT_CHOICES = [
        ('in', 'Inches'),
        ('cm', 'Centimeters'),
    ]

    measurement_system = models.CharField(max_length=2, choices=MEASUREMENT_CHOICES, default='cm')
    chamber_width = models.DecimalField(max_digits=6, decimal_places=2)
    chamber_height = models.DecimalField(max_digits=6, decimal_places=2)
    chamber_length = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def chamber_volume(self):
        volume = self.chamber_width * self.chamber_height * self.chamber_length
        if self.measurement_system == 'in':
            return volume  # return volume in cubic inches
        else:
            return volume / 16.387  # convert cubic inches to cubic centimeters


    def save(self, *args, **kwargs):
        '''
        If name is empty, count existing Growth Chambers for this user
        and generate a default name to save.
        '''
        if not self.name:
            count = GrowthChamber.objects.filter(user=self.user).count()
            self.name = f'GrowthChamber{count + 1}'
        if not self.device_type:
            self.device_type = ContentType.objects.get_for_model(self.__class__)
        super().save(*args, **kwargs)


class GeographicDiv(models.Model):
    tsn = models.IntegerField(primary_key=True)
    geographic_value = models.CharField(max_length=45)
    update_date = models.DateField()


class Hierarchy(models.Model):
    hierarchy_string = models.CharField(max_length=300)
    tsn = models.IntegerField(primary_key=True)
    parent_tsn = models.IntegerField(null=True)
    level = models.IntegerField()
    childrencount = models.IntegerField()


class Jurisdiction(models.Model):
    tsn = models.IntegerField(primary_key=True)
    jurisdiction_value = models.CharField(max_length=30)
    origin = models.CharField(max_length=19)
    update_date = models.DateField()


class Kingdoms(models.Model):
    kingdom_id = models.IntegerField(primary_key=True)
    kingdom_name = models.CharField(max_length=10)
    update_date = models.DateField()


class Longnames(models.Model):
    tsn = models.IntegerField(primary_key=True)
    completename = models.CharField(max_length=300)

class OtherSources(models.Model):
    source_id_prefix = models.CharField(max_length=3)
    source_id = models.IntegerField()
    source_type = models.CharField(max_length=10)
    source = models.CharField(max_length=64)
    version = models.CharField(max_length=10)
    acquisition_date = models.DateField()
    source_comment = models.CharField(max_length=500, null=True)
    update_date = models.DateField()


class NodcIds(models.Model):
    nodc_id = models.CharField(max_length=12)
    update_date = models.DateField()
    tsn = models.IntegerField()


class Publications(models.Model):
    pub_id_prefix = models.CharField(max_length=3)
    publication_id = models.IntegerField()
    reference_author = models.CharField(max_length=100)
    title = models.CharField(max_length=255, null=True)
    publication_name = models.CharField(max_length=255)
    listed_pub_date = models.DateField(null=True)
    actual_pub_date = models.DateField()
    publisher = models.CharField(max_length=80, null=True)
    pub_place = models.CharField(max_length=40, null=True)
    isbn = models.CharField(max_length=16, null=True)
    issn = models.CharField(max_length=16, null=True)
    pages = models.CharField(max_length=15, null=True)
    pub_comment = models.CharField(max_length=500, null=True)
    update_date = models.DateField()


class ReferenceLinks(models.Model):
    tsn = models.IntegerField()
    doc_id_prefix = models.CharField(max_length=3)
    documentation_id = models.IntegerField()
    original_desc_ind = models.CharField(max_length=1, null=True)
    init_itis_desc_ind = models.CharField(max_length=1, null=True)
    change_track_id = models.IntegerField(null=True)
    vernacular_name = models.CharField(max_length=80, null=True)
    update_date = models.DateField()


class SynonymLinks(models.Model):
    tsn = models.IntegerField()
    tsn_accepted = models.IntegerField()
    update_date = models.DateField()


class StrippedAuthor(models.Model):
    taxon_author_id = models.IntegerField()
    shortauthor = models.CharField(max_length=100)


class TaxonAuthorsLkp(models.Model):
    taxon_author_id = models.IntegerField()
    taxon_author = models.CharField(max_length=100)
    update_date = models.DateField()
    kingdom_id = models.SmallIntegerField()
    short_author = models.TextField()


class TaxonUnitTypes(models.Model):
    kingdom_id = models.IntegerField()
    rank_id = models.SmallIntegerField()
    rank_name = models.CharField(max_length=15)
    dir_parent_rank_id = models.SmallIntegerField()
    req_parent_rank_id = models.SmallIntegerField()
    update_date = models.DateField()


class TaxonomicUnits(models.Model):
    tsn = models.IntegerField()
    unit_ind1 = models.CharField(max_length=1, null=True)
    unit_name1 = models.CharField(max_length=35)
    unit_ind2 = models.CharField(max_length=1, null=True)
    unit_name2 = models.CharField(max_length=35, null=True)
    unit_ind3 = models.CharField(max_length=7, null=True)
    unit_name3 = models.CharField(max_length=35, null=True)
    unit_ind4 = models.CharField(max_length=7, null=True)
    unit_name4 = models.CharField(max_length=35, null=True)
    unnamed_taxon_ind = models.CharField(max_length=1, null=True)
    name_usage = models.CharField(max_length=12)
    unaccept_reason = models.CharField(max_length=50, null=True)
    credibility_rtng = models.CharField(max_length=40)
    completeness_rtng = models.CharField(max_length=10, null=True)
    currency_rating = models.CharField(max_length=7, null=True)
    phylo_sort_seq = models.SmallIntegerField(null=True)
    initial_time_stamp = models.DateTimeField()
    parent_tsn = models.IntegerField(null=True)
    taxon_author_id = models.IntegerField(null=True)
    hybrid_author_id = models.IntegerField(null=True)
    kingdom_id = models.SmallIntegerField()
    rank_id = models.SmallIntegerField()
    update_date = models.DateField()
    uncertain_prnt_ind = models.CharField(max_length=3, null=True)
    n_usage = models.TextField(null=True)
    complete_name = models.CharField(max_length=255)


class TuCommentsLinks(models.Model):
    tsn = models.IntegerField()
    comment_id = models.IntegerField()
    update_date = models.DateField()


class VernRefLinks(models.Model):
    tsn = models.IntegerField()
    doc_id_prefix = models.CharField(max_length=3)
    documentation_id = models.IntegerField()
    update_date = models.DateField()
    vern_id = models.IntegerField()


class Vernaculars(models.Model):
    tsn = models.IntegerField()
    vernacular_name = models.CharField(max_length=80)
    language = models.CharField(max_length=15)
    approved_ind = models.CharField(max_length=1, null=True)
    update_date = models.DateField()
    vern_id = models.IntegerField()

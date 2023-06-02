# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CatalogPlant(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'catalog_plant'


class CybotanyGrowthchamber(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    measurement_system = models.CharField(max_length=2)
    chamber_width = models.DecimalField(max_digits=6, decimal_places=2)
    chamber_height = models.DecimalField(max_digits=6, decimal_places=2)
    chamber_length = models.DecimalField(max_digits=6, decimal_places=2)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cybotany_growthchamber'


class CybotanyGrowthchamberInstruments(models.Model):
    id = models.BigAutoField(primary_key=True)
    growthchamber = models.ForeignKey(CybotanyGrowthchamber, models.DO_NOTHING)
    instrument = models.ForeignKey('CybotanyInstrument', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cybotany_growthchamber_instruments'
        unique_together = (('growthchamber', 'instrument'),)


class CybotanyGrowthchamberSensors(models.Model):
    id = models.BigAutoField(primary_key=True)
    growthchamber = models.ForeignKey(CybotanyGrowthchamber, models.DO_NOTHING)
    sensor = models.ForeignKey('CybotanySensor', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cybotany_growthchamber_sensors'
        unique_together = (('growthchamber', 'sensor'),)


class CybotanyInstrument(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'cybotany_instrument'


class CybotanySensor(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    description = models.TextField()
    max_value = models.DecimalField(max_digits=6, decimal_places=2)
    min_value = models.DecimalField(max_digits=6, decimal_places=2)
    value_unit = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'cybotany_sensor'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GeographicDiv(models.Model):
    tsn = models.IntegerField()
    geographic_value = models.CharField(max_length=45)
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'geographic_div'


class Hierarchy(models.Model):
    hierarchy_string = models.CharField(max_length=300)
    tsn = models.IntegerField()
    parent_tsn = models.IntegerField(blank=True, null=True)
    level = models.IntegerField()
    childrencount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hierarchy'


class Jurisdiction(models.Model):
    tsn = models.IntegerField()
    jurisdiction_value = models.CharField(max_length=30)
    origin = models.CharField(max_length=19)
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'jurisdiction'


class Kingdoms(models.Model):
    kingdom_id = models.IntegerField()
    kingdom_name = models.CharField(max_length=10)
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'kingdoms'


class Longnames(models.Model):
    tsn = models.IntegerField()
    completename = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'longnames'


class NodcIds(models.Model):
    nodc_id = models.CharField(max_length=12)
    update_date = models.DateField()
    tsn = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nodc_ids'


class OtherSources(models.Model):
    source_id_prefix = models.CharField(max_length=3)
    source_id = models.IntegerField()
    source_type = models.CharField(max_length=10)
    source = models.CharField(max_length=64)
    version = models.CharField(max_length=10)
    acquisition_date = models.DateField()
    source_comment = models.CharField(max_length=500, blank=True, null=True)
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'other_sources'


class Publications(models.Model):
    pub_id_prefix = models.CharField(max_length=3)
    publication_id = models.IntegerField()
    reference_author = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True, null=True)
    publication_name = models.CharField(max_length=255)
    listed_pub_date = models.DateField(blank=True, null=True)
    actual_pub_date = models.DateField()
    publisher = models.CharField(max_length=80, blank=True, null=True)
    pub_place = models.CharField(max_length=40, blank=True, null=True)
    isbn = models.CharField(max_length=16, blank=True, null=True)
    issn = models.CharField(max_length=16, blank=True, null=True)
    pages = models.CharField(max_length=15, blank=True, null=True)
    pub_comment = models.CharField(max_length=500, blank=True, null=True)
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'publications'


class ReferenceLinks(models.Model):
    tsn = models.IntegerField()
    doc_id_prefix = models.CharField(max_length=3)
    documentation_id = models.IntegerField()
    original_desc_ind = models.CharField(max_length=1, blank=True, null=True)
    init_itis_desc_ind = models.CharField(max_length=1, blank=True, null=True)
    change_track_id = models.IntegerField(blank=True, null=True)
    vernacular_name = models.CharField(max_length=80, blank=True, null=True)
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'reference_links'


class Strippedauthor(models.Model):
    taxon_author_id = models.IntegerField()
    shortauthor = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'strippedauthor'


class SynonymLinks(models.Model):
    tsn = models.IntegerField()
    tsn_accepted = models.IntegerField()
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'synonym_links'


class TaxonAuthorsLkp(models.Model):
    taxon_author_id = models.IntegerField()
    taxon_author = models.CharField(max_length=100)
    update_date = models.DateField()
    kingdom_id = models.SmallIntegerField()
    short_author = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'taxon_authors_lkp'


class TaxonUnitTypes(models.Model):
    kingdom_id = models.IntegerField()
    rank_id = models.SmallIntegerField()
    rank_name = models.CharField(max_length=15)
    dir_parent_rank_id = models.SmallIntegerField()
    req_parent_rank_id = models.SmallIntegerField()
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'taxon_unit_types'


class TaxonomicUnits(models.Model):
    tsn = models.IntegerField()
    unit_ind1 = models.CharField(max_length=1, blank=True, null=True)
    unit_name1 = models.CharField(max_length=35)
    unit_ind2 = models.CharField(max_length=1, blank=True, null=True)
    unit_name2 = models.CharField(max_length=35, blank=True, null=True)
    unit_ind3 = models.CharField(max_length=7, blank=True, null=True)
    unit_name3 = models.CharField(max_length=35, blank=True, null=True)
    unit_ind4 = models.CharField(max_length=7, blank=True, null=True)
    unit_name4 = models.CharField(max_length=35, blank=True, null=True)
    unnamed_taxon_ind = models.CharField(max_length=1, blank=True, null=True)
    name_usage = models.CharField(max_length=12)
    unaccept_reason = models.CharField(max_length=50, blank=True, null=True)
    credibility_rtng = models.CharField(max_length=40)
    completeness_rtng = models.CharField(max_length=10, blank=True, null=True)
    currency_rating = models.CharField(max_length=7, blank=True, null=True)
    phylo_sort_seq = models.SmallIntegerField(blank=True, null=True)
    initial_time_stamp = models.DateTimeField()
    parent_tsn = models.IntegerField(blank=True, null=True)
    taxon_author_id = models.IntegerField(blank=True, null=True)
    hybrid_author_id = models.IntegerField(blank=True, null=True)
    kingdom_id = models.SmallIntegerField()
    rank_id = models.SmallIntegerField()
    update_date = models.DateField()
    uncertain_prnt_ind = models.CharField(max_length=3, blank=True, null=True)
    n_usage = models.TextField(blank=True, null=True)
    complete_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'taxonomic_units'


class TuCommentsLinks(models.Model):
    tsn = models.IntegerField()
    comment_id = models.IntegerField()
    update_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'tu_comments_links'


class VernRefLinks(models.Model):
    tsn = models.IntegerField()
    doc_id_prefix = models.CharField(max_length=3)
    documentation_id = models.IntegerField()
    update_date = models.DateField()
    vern_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vern_ref_links'


class Vernaculars(models.Model):
    tsn = models.IntegerField()
    vernacular_name = models.CharField(max_length=80)
    language = models.CharField(max_length=15)
    approved_ind = models.CharField(max_length=1, blank=True, null=True)
    update_date = models.DateField()
    vern_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'vernaculars'

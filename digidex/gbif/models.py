from django.db import models


class Taxon(models.Model):
    taxon_id = models.BigIntegerField(
        primary_key=True
    )
    dataset_id = models.CharField(
        max_length=255
    )
    parent_name_usage_id = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    accepted_name_usage_id = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    original_name_usage_id = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    scientific_name = models.CharField(
        max_length=255
    )
    scientific_name_authorship = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    canonical_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    generic_name = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    specific_epithet = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    infraspecific_epithet = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    taxon_rank = models.CharField(
        max_length=255
    )
    name_according_to = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    name_published_in = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    taxonomic_status = models.CharField(
        max_length=255
    )
    nomenclatural_status = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    taxon_remarks = models.TextField(
        null=True,
        blank=True
    )
    kingdom = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    phylum = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    class_field = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )  # 'class' is a reserved keyword
    order = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    family = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    genus = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.scientific_name


class TypesAndSpecimen(models.Model):
    taxon = models.ForeignKey(
        Taxon,
        on_delete=models.CASCADE,
        related_name='types_and_specimens'
    )
    type_designation_type = models.CharField(
        max_length=255
    )
    type_designated_by = models.CharField(
        max_length=255
    )
    scientific_name = models.CharField(
        max_length=255
    )
    taxon_rank = models.CharField(
        max_length=255
    )
    source = models.CharField(
        max_length=255
    )

    def __str__(self):
        return f"{self.scientific_name} - {self.type_designation_type}"


class Description(models.Model):
    taxon = models.ForeignKey(
        Taxon,
        on_delete=models.CASCADE,
        related_name='descriptions'
    )
    type = models.CharField(
        max_length=255
    )
    language = models.CharField(
        max_length=255
    )
    description = models.TextField()
    source = models.CharField(
        max_length=255
    )
    creator = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    contributor = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    license = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.type} - {self.language}"


class Reference(models.Model):
    taxon = models.ForeignKey(
        Taxon,
        on_delete=models.CASCADE,
        related_name='references')
    bibliographic_citation = models.TextField()
    identifier = models.CharField(
        max_length=255
    )
    references = models.TextField(
        null=True,
        blank=True
    )
    source = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.bibliographic_citation


class Multimedia(models.Model):
    taxon = models.ForeignKey(
        Taxon,
        on_delete=models.CASCADE,
        related_name='multimedia'
    )
    identifier = models.CharField(
        max_length=255
    )
    references = models.TextField(
        null=True,
        blank=True
    )
    title = models.CharField(
        max_length=255
    )
    description = models.TextField(
        null=True,
        blank=True
    )
    license = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    creator = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    created = models.DateTimeField(
        null=True,
        blank=True
    )
    contributor = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    publisher = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    rights_holder = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    source = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class VernacularName(models.Model):
    taxon = models.ForeignKey(
        Taxon,
        on_delete=models.CASCADE,
        related_name='vernacular_names'
    )
    vernacular_name = models.CharField(
        max_length=255
    )
    language = models.CharField(
        max_length=255
    )
    country = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    country_code = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    sex = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    life_stage = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    source = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.vernacular_name


class Distribution(models.Model):
    taxon = models.ForeignKey(
        Taxon,
        on_delete=models.CASCADE,
        related_name='distributions'
    )
    location_id = models.CharField(
        max_length=255
    )
    locality = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    country = models.CharField(
        max_length=255
    )
    country_code = models.CharField(
        max_length=255
    )
    location_remarks = models.TextField(
        null=True,
        blank=True
    )
    establishment_means = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    life_stage = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    occurrence_status = models.CharField(
        max_length=255
    )
    threat_status = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )
    source = models.CharField(
        max_length=255
    )

    def __str__(self):
        return self.locality or self.location_id

from django.db import models
from .nfc import NFC

class NTAG(NFC):
    """
    Model representing NTAGs, a specific implementation of NFC tags.
    Inherits common attributes from NFC and can include NTAG-specific fields and methods.
    """
    NTAG_TYPES = [
        ('NTAG_424_DNA_TagTamper', 'NTAG 424 DNA TagTamper'),
        ('NTAG_424_DNA', 'NTAG 424 DNA'),
        ('NTAG_426Q_DNA', 'NTAG 426Q DNA'),
        ('NTAG_223_DNA', 'NTAG 223 DNA'),
        ('NTAG_224_DNA', 'NTAG 224 DNA'),
        ('NTAG_223_DNA_StatusDetect', 'NTAG 223 DNA StatusDetect'),
        ('NTAG_224_DNA_StatusDetect', 'NTAG 224 DNA StatusDetect'),
        ('NTAG_213_TagTamper', 'NTAG 213 TagTamper'),
        ('NTAG_213', 'NTAG 213'),
        ('NTAG_215', 'NTAG 215'),
        ('NTAG_216', 'NTAG 216'),
        ('NTAG_210', 'NTAG 210'),
        ('NTAG_212', 'NTAG 212'),
    ]

    NTAG_USES = [
        ('plant_label', 'Plant Label'),
        ('pet_tag', 'Pet Tag'),
    ]

    ntag_type = models.CharField(
        max_length=25,
        blank=True,
        choices=NTAG_TYPES, 
        default='NTAG_213'
        verbose_name="NTAG Type",
        help_text="The type of the NTAG."
    )
    ntag_use = models.CharField(
        max_length=20,
        choices=NTAG_USES,
        default='plant_label'
        verbose_name="NTAG Use",
        help_text="The intended use of the NTAG."
    )

    def __str__(self):
        """
        Returns a string representation of the NTAG instance, primarily based on its unique serial number.
        """
        return f"{self.ntag_type} - {self.serial_number}"

    class Meta:
        verbose_name = "NTAG"
        verbose_name_plural = "NTAGs"

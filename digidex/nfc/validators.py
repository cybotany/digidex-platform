from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

module_format_validator = RegexValidator(
    regex='^([0-9A-Fa-f]{2}:)+$',
    message="Each component of the serial number must be two hexadecimal characters followed by a colon.",
    code='invalid_module_format'
)

@deconstructible
class ComponentCountValidator:
    def __init__(self, count):
        self.count = count

    def __call__(self, value):
        actual_count = len(value.split(':')) - 1
        if actual_count != self.count:
            raise ValidationError(
                _("Ensure the serial number contains exactly %(count)d components (found %(actual_count)d)."),
                params={'count': self.count, 'actual_count': actual_count},
                code='invalid_component_count'
            )

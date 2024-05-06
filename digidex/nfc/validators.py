from django.core.validators import RegexValidator
from django.core.validators import BaseValidator
from django.utils.deconstruct import deconstructible
from django.utils.translation import gettext_lazy as _

module_format_validator = RegexValidator(
    regex='^([0-9A-Fa-f]{2}:)+$',
    message="Each component of the serial number must be two hexadecimal characters followed by a colon.",
    code='invalid_module_format'
)

@deconstructible
class ComponentCountValidator(BaseValidator):
    compare = lambda self, a, b: a != b
    message = _("Ensure the serial number contains exactly %(limit_value)d components.")
    code = 'invalid_component_count'

    def clean(self, x):
        return len(x.split(':')) - 1

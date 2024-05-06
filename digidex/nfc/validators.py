from django.core.validators import RegexValidator

SERIAL_NUMBER_REGEX = '^([0-9A-Fa-f]{2}:){9}[0-9A-Fa-f]{2}$'

serial_number_validator = RegexValidator(
    regex=SERIAL_NUMBER_REGEX,
    message=_("Serial number must be in the format XX:XX:XX:XX:XX:XX:XX"),
    code='invalid_serial_number'
)

import re
from django.core.validators import RegexValidator

digidex_username_validator = RegexValidator(
    regex=r'^[\w-]+$',
    message="Username must contain only letters, digits, and dashes.",
    flags=re.ASCII
)

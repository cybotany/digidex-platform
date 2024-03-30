import re
from django.core.validators import RegexValidator

validate_username = RegexValidator(
    regex=r'^[\w-]+$',
    message="Username must contain only letters, digits, and dashes.",
    flags=re.ASCII
)

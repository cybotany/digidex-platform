import uuid
from django.db import models
from django.conf import settings


class UserParty(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False,
        db_index=True,
        verbose_name="Digitized Object UUID"
    )
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="party"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    def add_digit(self, digit):
        user_party_digit, created = UserPartyDigit.objects.get_or_create(
            user_party=self,
            digit=digit
        )
        return user_party_digit

    def get_all_digits(self):
        return self.digits.all() if self.digits.exists() else None


class UserPartyDigit(models.Model):
    user_party = models.ForeignKey(
        'party.UserParty',
        on_delete=models.CASCADE,
        related_name="digits"
    )
    digit = models.ForeignKey(
        'digitization.DigitalObject',
        on_delete=models.CASCADE,
        related_name="party"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified = models.DateTimeField(
        auto_now=True
    )

    @property
    def digit_name(self):
        return self.digit.digit_name

    @property
    def digit_description(self):
        if self.digit.digit_description:
            return self.digit.digit_description
        return "No description available."

    @property
    def digit_page(self):
        return self.digit.digit_page
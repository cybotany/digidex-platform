from django.db import models
from django.conf import settings
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)

class ConsentType(models.Model):
    name = models.CharField(
        max_length=100
    )
    description = models.TextField()

    panels = [
        FieldPanel('name'),
        FieldPanel('description'),
    ]

    def __str__(self):
        return self.name

class UserConsent(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    consent_type = models.ForeignKey(
        ConsentType,
        related_name="consents",
        on_delete=models.CASCADE
    )
    status = models.BooleanField(
        default=False
    )
    timestamp = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = ('user', 'consent_type',)


class ConsentTypeAdmin(ModelAdmin):
    model = ConsentType
    menu_label = 'Consent Types'
    menu_icon = 'placeholder'
    menu_order = 200
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ('name', 'description')
    search_fields = ('name', 'description')

modeladmin_register(ConsentTypeAdmin)

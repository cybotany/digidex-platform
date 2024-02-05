from django.contrib import admin
from digidex.inventory.models import Digit

@admin.register(Digit)
class DigitAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'taxonomic_unit', 'nfc_link', 'journal_collection', 'created_at', 'last_modified', 'is_public', 'is_archived')
    list_filter = ('is_public', 'is_archived', 'created_at', 'last_modified')
    search_fields = ('name', 'uuid', 'nfc_link__serial_number')
    readonly_fields = ('uuid', 'created_at', 'last_modified')
    fieldsets = (
        (None, {
            'fields': ('uuid', 'name', 'description', 'taxonomic_unit', 'nfc_link', 'journal_collection')
        }),
        ('Status', {
            'fields': ('is_public', 'is_archived')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_modified')
        }),
    )
    actions = ['archive_digits', 'unarchive_digits']

    @admin.action(description='Archive selected digits')
    def archive_digits(self, request, queryset):
        queryset.update(is_archived=True)

    @admin.action(description='Unarchive selected digits')
    def unarchive_digits(self, request, queryset):
        queryset.update(is_archived=False)

    def save_model(self, request, obj, form, change):
        # Custom save logic can be added here
        super().save_model(request, obj, form, change)

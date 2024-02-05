from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from digidex.inventory.models import Digit

@admin.register(Digit)
class DigitAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'taxonomic_unit', 'nfc_link_detail', 'journal_collection_link', 'entry_count', 'created_at', 'last_modified', 'is_public', 'is_archived')
    list_filter = ('is_public', 'is_archived', 'created_at', 'last_modified')
    search_fields = ('name', 'uuid', 'nfc_link__serial_number')
    readonly_fields = ('uuid', 'nfc_link_detail', 'journal_collection_link', 'entry_count', 'created_at', 'last_modified')
    fieldsets = (
        (None, {
            'fields': ('uuid', 'name', 'description', 'taxonomic_unit', 'nfc_link', 'nfc_link_detail', 'journal_collection', 'journal_collection_link', 'entry_count')
        }),
        ('Status', {
            'fields': ('is_public', 'is_archived')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_modified')
        }),
    )
    actions = ['archive_digits', 'unarchive_digits']

    def nfc_link_detail(self, obj):
        if obj.nfc_link:
            return format_html('<a href="{}">{} (Serial: {})</a>', reverse('admin:link_nfc_change', args=[obj.nfc_link.id]), "NFC Link", obj.nfc_link.serial_number)
        return "No NFC Link"
    nfc_link_detail.short_description = 'NFC Link Detail'

    def journal_collection_link(self, obj):
        if obj.journal_collection:
            url = reverse('admin:journal_collection_change', args=[obj.journal_collection.id])
            return format_html('<a href="{}">Collection ID: {}</a>', url, obj.journal_collection.id)
        return "No Collection"
    journal_collection_link.short_description = 'Journal Collection'

    def entry_count(self, obj):
        if obj.journal_collection:
            return obj.journal_collection.entries.count()
        return 0
    entry_count.short_description = 'Number of Journal Entries'

    @admin.action(description='Archive selected digits')
    def archive_digits(self, request, queryset):
        queryset.update(is_archived=True)

    @admin.action(description='Unarchive selected digits')
    def unarchive_digits(self, request, queryset):
        queryset.update(is_archived=False)

    def save_model(self, request, obj, form, change):
        # Custom save logic can be added here
        super().save_model(request, obj, form, change)

    class Media:
        css = {
            'all': ('your-custom-css-path.css',)
        }

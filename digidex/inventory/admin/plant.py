from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from digidex.inventory.models import Plant

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid', 'taxon', 'ntag_detail', 'journal_collection_link', 'entry_count', 'created_at', 'last_modified', 'is_archived')
    list_filter = ('is_archived', 'created_at', 'last_modified')
    search_fields = ('name', 'uuid', 'ntag__serial_number')
    readonly_fields = ('uuid', 'ntag_detail', 'journal_collection_link', 'entry_count', 'created_at', 'last_modified')
    fieldsets = (
        (None, {
            'fields': ('uuid', 'name', 'description', 'taxon', 'ntag', 'ntag_detail', 'journal_collection', 'journal_collection_link', 'entry_count')
        }),
        ('Status', {
            'fields': ('is_archived',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_modified')
        }),
    )
    actions = ['archive_items', 'unarchive_items']

    def ntag_detail(self, obj):
        if obj.ntag:
            return format_html('<a href="{}">{} (Serial: {})</a>', reverse('admin:link_ntag_change', args=[obj.ntag.id]), "NTAG Link", obj.ntag.serial_number)
        return "No NTAG Link"
    ntag_detail.short_description = 'NTAG Link Detail'

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

    @admin.action(description='Archive selected items')
    def archive_items(self, request, queryset):
        queryset.update(is_archived=True)

    @admin.action(description='Unarchive selected items')
    def unarchive_items(self, request, queryset):
        queryset.update(is_archived=False)

from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from digidex.journal.models import Entry

@admin.register(Entry)
class JournalEntry(admin.ModelAdmin):
    list_display = ('entry_number', 'collection_link', 'content_summary', 'image_thumbnail', 'created_at', 'last_modified')
    list_filter = ('created_at', 'last_modified', 'collection__id')
    search_fields = ('content', 'collection__id')
    readonly_fields = ('entry_number', 'created_at', 'last_modified', 'image_thumbnail')
    fieldsets = (
        (None, {
            'fields': ('collection', 'entry_number', 'content', 'image')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_modified')
        }),
    )

    def collection_link(self, obj):
        return format_html('<a href="{}">{}</a>', reverse('admin:journal_collection_change', args=[obj.collection.id]), obj.collection)
    collection_link.short_description = 'Collection'

    def content_summary(self, obj):
        return obj.content[:50] + '...' if obj.content else 'No Content'
    content_summary.short_description = 'Content Summary'

    def image_thumbnail(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image.url)
        return "No Image"
    image_thumbnail.short_description = 'Image'


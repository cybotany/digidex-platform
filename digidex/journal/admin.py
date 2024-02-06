from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from digidex.journal.models import Entry, Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'thumbnail_image', 'get_digit_name', 'get_entry_count', 'view_entries_link', 'created_at', 'last_modified')
    list_filter = ('created_at', 'last_modified')
    search_fields = ('digit__name', 'entries__content')
    readonly_fields = ('created_at', 'last_modified', 'thumbnail_image', 'view_entries_link')
    fieldsets = (
        (None, {
            'fields': ('thumbnail', 'thumbnail_image')
        }),
        ('Related Digit', {
            'fields': ('get_digit_name', 'get_digit_description', 'view_entries_link')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_modified')
        }),
    )

    def get_queryset(self, request):
        # Prefetch related data for efficient querying
        return super().get_queryset(request).prefetch_related('digit', 'entries')

    def thumbnail_image(self, obj):
        if obj.thumbnail and obj.thumbnail.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.thumbnail.image.url)
        return "No Image"
    thumbnail_image.short_description = 'Thumbnail Image'

    def view_entries_link(self, obj):
        count = obj.entries.count()
        url = reverse('admin:journal_entry_changelist') + f'?collection__id__exact={obj.id}'
        return format_html('<a href="{}">{} Entries</a>', url, count)
    view_entries_link.short_description = 'View Entries'

    def get_digit_name(self, obj):
        return obj.get_digit_name()
    get_digit_name.short_description = 'Digit Name'

    def get_digit_description(self, obj):
        return obj.get_digit_description()
    get_digit_description.short_description = 'Digit Description'

    def get_entry_count(self, obj):
        return obj.get_entry_count()
    get_entry_count.short_description = 'Number of Entries'


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
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


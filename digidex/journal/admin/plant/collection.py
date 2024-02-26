from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from digidex.journal.models import Collection


@admin.register(Collection)
class PlantCollection(admin.ModelAdmin):
    list_display = ('id', 'thumbnail_image', 'get_entity_name', 'get_entry_count', 'view_entries_link', 'created_at', 'last_modified')
    list_filter = ('created_at', 'last_modified')
    search_fields = ('plant__name', 'entries__content')
    readonly_fields = ('created_at', 'last_modified', 'thumbnail_image', 'view_entries_link')
    fieldsets = (
        (None, {
            'fields': ('thumbnail', 'thumbnail_image')
        }),
        ('Related Plant', {
            'fields': ('get_entity_name', 'get_entity_description', 'view_entries_link')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_modified')
        }),
    )

    def get_queryset(self, request):
        # Prefetch related data for efficient querying
        return super().get_queryset(request).prefetch_related('plant', 'entries')

    def thumbnail_image(self, obj):
        if obj.thumbnail and obj.thumbnail.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.thumbnail.image.url)
        return "No Image"
    thumbnail_image.short_description = 'Thumbnail Image'

    def view_entries_link(self, obj):
        count = obj.get_entry_count
        url = reverse('admin:journal_entry_changelist') + f'?collection__id__exact={obj.id}'
        return format_html('<a href="{}">{} Entries</a>', url, count)
    view_entries_link.short_description = 'View Entries'

    def get_entity_name(self, obj):
        return obj.get_entity_name()
    get_entity_name.short_description = 'Plant Name'

    def get_entity_description(self, obj):
        return obj.get_entity_description()
    get_entity_description.short_description = 'Plant Description'

    def get_entry_count(self, obj):
        return obj.get_entry_count()
    get_entry_count.short_description = 'Number of Entries'

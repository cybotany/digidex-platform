from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q

from digidex.inventory.models import Pet, Plant
from digidex.journal.models import collection as base_collection


@admin.register(base_collection.Collection)
class JournalCollection(admin.ModelAdmin):
    list_display = ('id', 'thumbnail_image', 'get_entity_name', 'get_entry_count', 'view_entries_link', 'created_at', 'last_modified')
    list_filter = ('created_at', 'last_modified')
    search_fields = []
    readonly_fields = ('created_at', 'last_modified', 'thumbnail_image', 'view_entries_link')
    fieldsets = (
        (None, {
            'fields': ('thumbnail', 'thumbnail_image')
        }),
        ('Related Entity', {
            'fields': ('get_entity_name', 'get_entity_description', 'view_entries_link')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'last_modified')
        }),
    )
    def get_search_results(self, request, queryset, search_term):
        # Original search results, without considering the generic relation
        queryset, use_distinct = super().get_search_results(request, queryset, search_term)

        if search_term:
            # Get content types for Pet and Plant
            pet_ct = ContentType.objects.get_for_model(Pet)
            plant_ct = ContentType.objects.get_for_model(Plant)

            # Search in Pet and Plant models
            pet_ids = Pet.objects.filter(name__icontains=search_term).values_list('id', flat=True)
            plant_ids = Plant.objects.filter(name__icontains=search_term).values_list('id', flat=True)

            # Filter collections by object_id and content_type
            queryset |= self.model.objects.filter(
                Q(object_id__in=pet_ids, content_type=pet_ct) | 
                Q(object_id__in=plant_ids, content_type=plant_ct)
            )
        return queryset, use_distinct

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('entries')

    def thumbnail_image(self, obj):
        if obj.thumbnail and obj.thumbnail.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.thumbnail.image.url)
        return "No Image"
    thumbnail_image.short_description = 'Thumbnail Image'

    def view_entries_link(self, obj):
        count = obj.get_entry_count()
        url = reverse('admin:journal_entry_changelist') + f'?collection__id__exact={obj.id}'
        return format_html('<a href="{}">{} Entries</a>', url, count)
    view_entries_link.short_description = 'View Entries'

    def get_entity_name(self, obj):
        return obj.get_entity_name()
    get_entity_name.short_description = 'Entity Name'

    def get_entity_description(self, obj):
        return obj.get_entity_description()
    get_entity_description.short_description = 'Entity Description'

    def get_entry_count(self, obj):
        return obj.get_entry_count()
    get_entry_count.short_description = 'Number of Entries'

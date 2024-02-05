from django.contrib import admin
from digidex.link.models import NFC

@admin.register(NFC)
class NFCAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'counter', 'user', 'active', 'created_at', 'last_modified')
    list_filter = ('active', 'created_at', 'last_modified')
    search_fields = ('serial_number', 'user__username')
    actions = ['activate_links', 'deactivate_links']

    @admin.action(description='Activate selected NFC links')
    def activate_links(self, request, queryset):
        queryset.update(active=True)

    @admin.action(description='Deactivate selected NFC links')
    def deactivate_links(self, request, queryset):
        queryset.update(active=False)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

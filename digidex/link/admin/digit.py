from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from digidex.link.models import NTAG

@admin.register(NTAG)
class DigitLink(admin.ModelAdmin):
    list_display = ('serial_number', 'ntag_type', 'counter', 'user_link', 'active', 'created_at', 'last_modified')
    list_filter = ('ntag_type', 'active', 'created_at', 'last_modified', 'user__username')
    search_fields = ('serial_number', 'user__username')
    actions = ['activate_links', 'deactivate_links']
    readonly_fields = ('user_link',)

    def user_link(self, obj):
        if obj.user:
            return format_html('<a href="{}">{}</a>', reverse('admin:accounts_user_change', args=[obj.user.id]), obj.user.username)
        return "No User"
    user_link.short_description = 'User'

    def digit_link(self, obj):
        return "Adjust or remove this method based on NTAG-Digit relationship"

    @admin.action(description='Activate selected NTAG links')
    def activate_links(self, request, queryset):
        queryset.update(active=True)

    @admin.action(description='Deactivate selected NTAG links')
    def deactivate_links(self, request, queryset):
        queryset.update(active=False)

    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)

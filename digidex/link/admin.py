from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from digidex.link.models import NFC

@admin.register(NFC)
class NFCAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'counter', 'user_link', 'digit_link', 'active', 'created_at', 'last_modified')
    list_filter = ('active', 'created_at', 'last_modified', 'user__username')
    search_fields = ('serial_number', 'user__username', 'digit__name')
    actions = ['activate_links', 'deactivate_links']
    readonly_fields = ('user_link', 'digit_link')

    def user_link(self, obj):
        if obj.user:
            return format_html('<a href="{}">{}</a>', reverse('admin:accounts_user_change', args=[obj.user.id]), obj.user.username)
        return "No User"
    user_link.short_description = 'User'

    def digit_link(self, obj):
        digit = obj.digit_set.first()  # Assuming a OneToOne relationship from Digit to NFC
        if digit:
            return format_html('<a href="{}">{}</a>', reverse('admin:inventory_digit_change', args=[digit.id]), digit.name)
        return "No Digit"
    digit_link.short_description = 'Associated Digit'

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

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from django.urls import reverse
from digidex.accounts.models import User

class UserAdmin(BaseUserAdmin):
    model = User

    # Define custom fieldsets
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('uuid', 'email_confirmed', 'user_specific_info')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email_confirmed', 'user_specific_info')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'uuid', 'email_confirmed', 'digit_count', 'collection_count')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'email_confirmed')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'uuid')
    readonly_fields = ('uuid', 'digit_count', 'collection_count')

    def digit_count(self, user):
        return user.digits.count()
    digit_count.short_description = 'Number of Digits'

    def collection_count(self, user):
        return user.collections.count()
    collection_count.short_description = 'Number of Collections'

    def user_specific_info(self, user):
        # Add a link to a custom user detail page or any other related information
        url = reverse('custom_user_detail', args=[user.uuid])
        return format_html('<a href="{}">User Detail Page</a>', url)
    user_specific_info.short_description = 'More Info'

    # Implement custom actions if necessary

    def save_model(self, request, obj, form, change):
        # Custom save logic can be added here
        super().save_model(request, obj, form, change)

    # Optionally, override the get_queryset method to optimize query performance

    class Media:
        css = {
            'all': ('your-custom-css-path.css',)
        }

# Register your custom user admin
admin.site.register(User, UserAdmin)

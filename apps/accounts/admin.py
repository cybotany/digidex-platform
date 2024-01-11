from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    model = User

    # Define custom fieldsets
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('uuid', 'email_confirmed')}),
    )

    # Define additional fields to include in the User creation form in admin
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email_confirmed',)}),
    )

    # Include custom fields in the list display, list filter, and search
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'uuid', 'email_confirmed')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'email_confirmed')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'uuid')

    # Make uuid field read-only
    readonly_fields = ('uuid',)

# Register your custom user admin
admin.site.register(User, UserAdmin)

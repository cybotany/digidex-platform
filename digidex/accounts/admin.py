from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from digidex.accounts.models import user as base_user

class UserAccount(UserAdmin):
    model = base_user.User

    # Define custom fieldsets
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('uuid', 'email_confirmed')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email_confirmed')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'uuid', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'email_confirmed')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'uuid')
    ordering = ('date_joined','username')

# Register custom user admin
admin.site.register(base_user.User, UserAdmin)

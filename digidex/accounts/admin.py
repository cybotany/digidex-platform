from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from django.urls import reverse
from digidex.accounts.models import User

class UserAdmin(BaseUserAdmin):
    model = User

    # Define custom fieldsets
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('uuid', 'email_confirmed')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('email_confirmed')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'uuid', 'date_joined')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'email_confirmed')
    search_fields = ('username', 'first_name', 'last_name', 'email', 'uuid')
    ordering = ('date_joined','username')

# Register custom user admin
admin.site.register(User, UserAdmin)

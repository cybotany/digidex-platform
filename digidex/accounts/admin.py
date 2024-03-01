from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from digidex.accounts.models import user as digidex_user

class UserAccount(UserAdmin):
    model = digidex_user.DigidexUser

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

admin.site.register(digidex_user.DigidexUser, UserAdmin)

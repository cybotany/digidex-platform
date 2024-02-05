from django.contrib import admin
from digidex.main.models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'response_received')
    list_filter = ('created_at', 'response_received')
    search_fields = ('name', 'email')

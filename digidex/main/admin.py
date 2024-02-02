from django.contrib import admin
from django.http import HttpResponse
from digidex.main.models import Contact

def response_summary(modeladmin, request, queryset):
    summary = Contact.get_pending_responses_summary()
    response = HttpResponse(content_type='text/plain')
    response.write("Response Summary:\n")
    response.write(f"Contacts submitted within the last day: {summary['day_old']}\n")
    response.write(f"Contacts submitted within the last week: {summary['week_old']}\n")
    response.write(f"Contacts submitted within the last month: {summary['month_old']}\n")
    return response
response_summary.short_description = "Get response summary"

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at', 'response_received')
    list_filter = ('created_at', 'response_received')
    search_fields = ('name', 'email')

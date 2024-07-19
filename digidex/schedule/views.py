import calendar

from django.shortcuts import render
from django.utils import timezone
from django.urls import path

from wagtail.admin.viewsets.base import ViewSet, ViewSetGroup

from .models import Event


def index(request):
    current_year = timezone.now().year
    calendar_html = calendar.HTMLCalendar().formatyear(current_year)

    return render(request, 'wagtailcalendar/index.html', {
        'current_year': current_year,
        'calendar_html': calendar_html,
    })

def month(request):
    current_year = timezone.now().year
    current_month = timezone.now().month
    calendar_html = calendar.HTMLCalendar().formatmonth(current_year, current_month)

    return render(request, 'wagtailcalendar/index.html', {
        'current_year': current_year,
        'calendar_html': calendar_html,
    })

class CalendarViewSet(ViewSet):
    add_to_admin_menu = False
    menu_label = "Calendar"
    icon = "date"
    # The `name` will be used for both the URL prefix and the URL namespace.
    # They can be customised individually via `url_prefix` and `url_namespace`.
    name = "calendar"

    def get_urlpatterns(self):
        return [
            # This can be accessed at `/admin/calendar/`
            # and reverse-resolved with the name `calendar:index`.
            # This first URL will be used for the menu item, but it can be
            # customized by overriding the `menu_url` property.
            path('', index, name='index'),

            # This can be accessed at `/admin/calendar/month/`
            # and reverse-resolved with the name `calendar:month`.
            path('month/', month, name='month'),
        ]


def event_list(request):
    events = Event.objects.all()
    return render(request, 'wagtailcalendar/event_list.html', {
        'events': events,
    })

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'wagtailcalendar/event_detail.html', {
        'event': event,
    })


class EventViewSet(ViewSet):
    add_to_admin_menu = False
    menu_label = "Events"
    icon = "list-ul"
    name = "events"

    def get_urlpatterns(self):
        return [
            path('', event_list, name='event-list'),
            path('<int:event_id>/', event_detail, name='event-detail'),
        ]


class AgendaViewSetGroup(ViewSetGroup):
    menu_label = "Agenda"
    menu_icon = "table"
    # You can specify instances or subclasses of `ViewSet` in `items`.
    items = (CalendarViewSet(), EventViewSet)

import logging
logger = logging.getLogger(__name__)

from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from digidex.inventory.models import Grouping
from digidex.inventory.forms import GroupingForm

class AbstractGroupingView(View):
    model = Grouping
    form_class = GroupingForm
    success_url = '/'  # Redirect to homepage or another success page as default
    template_name = None  # To be defined in subclasses

    def get(self, request, *args, **kwargs):
        # Default GET implementation (can be overridden in subclasses)
        return render(request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        # Default POST implementation (to be customized in subclasses)
        form = self.form_class(request.POST)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_context_data(self, **kwargs):
        # Method to provide additional context data for rendering the templates
        context = kwargs
        context.setdefault('form', self.form_class())
        return context

    def form_valid(self, form):
        # Method to handle valid form submissions (to be customized in subclasses)
        # Placeholder implementation
        return HttpResponseRedirect(self.success_url)

    def form_invalid(self, form):
        # Method to handle invalid form submissions
        return render(self.request, self.template_name, {'form': form})

    def add_message(self, message_type, message):
        # Helper method to add messages
        if message_type == 'success':
            messages.success(self.request, message)
        elif message_type == 'error':
            messages.error(self.request, message)

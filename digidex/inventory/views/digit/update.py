import logging
from django.views.generic.edit import UpdateView
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from digidex.inventory.models import MODEL_MAP
from digidex.inventory.forms import FORM_MAP

logger = logging.getLogger(__name__)

class UpdateDigit(LoginRequiredMixin, UpdateView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        digit = context.get('object')
        context['type'] = digit.get_digit_type
        context['uuid'] = str(digit.uuid)
        return context
    
    def get_form_kwargs(self):
        """
        Return the keyword arguments for instantiating the form.
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_form_class(self):
        """
        Dynamically get the form class based on 'type' query parameter.
        """
        digit_type = self.kwargs.get('type')
        form_class = FORM_MAP.get(digit_type)
        if not form_class:
            raise Http404("Invalid digit type")
        return form_class

    def get_template_names(self):
        """
        Dynamically get the template name based on 'type' query parameter.
        """
        digit_type = self.kwargs.get('type')
        template_name = f'inventory/digit/{digit_type}/update-page.html'
        if not template_name:
            raise Http404("Invalid digit type")
        return [template_name]
    
    def get_object(self, queryset=None):
        digit_type = self.kwargs.get('type')
        uuid = self.kwargs.get('uuid')

        if not uuid or not digit_type:
            raise Http404("No uuid or digit type provided")

        model = MODEL_MAP.get(digit_type)
        if not model:
            raise Http404(f"Invalid digit type '{digit_type}'")

        obj = model.objects.filter(uuid=uuid).first()
        if obj:
            user = self.request.user
            if obj.ntag.user != user:
                raise PermissionDenied("You do not have permission to edit this item.")
            self.model = model
            return obj
        else:
            raise Http404("No matching object found")

    def form_valid(self, form):
        """
        If the form is valid, save the updated object and send a success message.
        """
        response = super().form_valid(form)
        messages.success(self.request, f"{self.model.__name__} updated successfully.")
        return response

    def form_invalid(self, form):
        """
        If the form is invalid, add an error message before re-rendering the form.
        """
        messages.error(self.request, "There was a problem with the form. Please check the details you entered.")
        return super().form_invalid(form)

    def get_success_url(self):
        """
        After successfully updating the object, redirect to the object's URL.
        """
        return self.object.get_absolute_url()

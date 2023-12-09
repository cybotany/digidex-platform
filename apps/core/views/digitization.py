from django.shortcuts import get_object_or_404
from django.views.generic.edit import CreateView
from apps.core.models import Digit
from apps.core.forms import CreateDigitForm
from apps.inventory.models import Link


class DigitizationView(CreateView):
    model = Digit
    form_class = CreateDigitForm
    template_name = 'create_digit.html'

    def get_form_kwargs(self):
        # Call the base implementation first to get a context
        kwargs = super(DigitizationView, self).get_form_kwargs()
        # Add in the user
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        # Retrieve the link instance using link_id from the URL
        link_id = self.kwargs.get('link_id')
        link = get_object_or_404(Link, id=link_id)

        # Set the digit instance to the form's instance and save
        digit = form.save(commit=False)
        digit.save()

        # Set the digit field of the Link instance
        link.digit = digit
        link.user = self.request.user

        if 'group' in form.cleaned_data:
            link.group = form.cleaned_data['group']

        link.active = True
        link.save()

        return super(DigitizationView, self).form_valid(form)

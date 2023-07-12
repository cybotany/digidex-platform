from django.contrib import messages
from django.db import IntegrityError
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.forms import GrowingLabelForm


class RegisterLabelView(FormView):
    template_name = 'botany/register_label.html'
    form_class = GrowingLabelForm

    def form_valid(self, form):
        try:
            new_label = form.save(commit=False)
            new_label.user = self.request.user
            new_label.save()

            Activity.objects.create(
                user=self.request.user,
                activity_status='registered',
                activity_type='growing_label',
                content=f'Registered a new label group: {new_label.name}',
            )

            messages.success(self.request, f'Label "{new_label.name}" was successfully added.')

        except IntegrityError:
            form.add_error('name', f'A label with the name "{form.cleaned_data["name"]}" already exists.')
            return self.form_invalid(form)

        return redirect('botany:home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

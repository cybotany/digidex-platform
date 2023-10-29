from django.contrib import messages
from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.forms import GrowingComponentForm


class RegisterComponentView(FormView):
    """
    View for registering a new growing medium component.
    """
    template_name = 'botany/register_component.html'
    form_class = GrowingComponentForm

    def form_valid(self, form):
        """
        If the submitted form is valid, save the info to the database and
        redirect the user to the growing medium component detail page.

        Returns:
            Redirects user to the growing medium component detail page of the submitted component.
        """
        new_component = form.save()

        Activity.objects.create(
            user=self.request.user,
            activity_status='registered',
            activity_type='growing_component',
            content=f'Registered a new growing medium component: {new_component.component}',
        )

        messages.success(self.request, f'Component "{new_component.name}" was successfully added.')
        return redirect('botany:home')

    def get_form_kwargs(self):
        """
        Pass the logged on user object to the GrowingComponentForm.

        Returns:
            kwargs dictionary with the key 'user' assigned to value self.request.user
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

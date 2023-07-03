from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.forms import GrowingMediumComponentForm


class CreateGrowingMediumComponentView(FormView):
    """
    View for creating a new growing medium component.
    """
    template_name = 'botany/create_growing_medium_component.html'
    form_class = GrowingMediumComponentForm

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
            activity_status='created',
            activity_type='growing_medium_component',
            content=f'Created a new growing medium component: {new_component.component}',
        )
        
        # Assuming the GrowingMediumComponent model has a get_absolute_url method
        return redirect(new_component.get_absolute_url())

    def get_form_kwargs(self):
        """
        Pass the logged on user object to the GrowingMediumComponentForm.

        Returns:
            kwargs dictionary with the key 'user' assigned to value self.request.user
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

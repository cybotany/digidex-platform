from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.forms import GrowingFertilizerForm


class RegisterFertilizerView(FormView):
    """
    View for registering a new fertilizer mix.
    """
    template_name = 'botany/register_fertilizer.html'
    form_class = GrowingFertilizerForm

    def form_valid(self, form):
        """
        If the submitted form is valid, save the info to the database and
        redirect the user to the fertilizer mix detail page.

        Returns:
            Redirects user to the fertilizer mix detail page of the submitted mix.
        """
        new_fertilizer_mix = form.save()

        Activity.objects.create(
            user=self.request.user,
            activity_status='registered',
            activity_type='fertilizer_mix',
            content=f'Registered a new fertilizer mix: {new_fertilizer_mix.name}',
        )

        return redirect(new_fertilizer_mix.get_absolute_url())

    def get_form_kwargs(self):
        """
        Pass the logged on user object to the FertilizerMixForm.

        Returns:
            kwargs dictionary with the key 'user' assigned to value self.request.user
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

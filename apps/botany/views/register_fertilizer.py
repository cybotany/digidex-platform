from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.forms import GrowingMediumForm, GrowingComponentForm


class RegisterGrowingMediumView(FormView):
    """
    View for registering a new growing medium.
    """
    template_name = 'botany/register_medium.html'
    form_class = GrowingMediumForm

    def get_context_data(self, **kwargs):
        context = super(RegisterGrowingMediumView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = GrowingComponentForm(self.request.POST)
        else:
            context['formset'] = GrowingComponentForm()
        return context

    def form_valid(self, form):
        """
        If the submitted form is valid, save the info to the database and
        redirect the user to the growing medium detail page.

        Returns:
            Redirects user to the growing medium detail page of the submitted medium.
        """
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            new_growing_medium = form.save()
            formset.instance = new_growing_medium
            formset.save()

            Activity.objects.create(
                user=self.request.user,
                activity_status='registered',
                activity_type='growing_medium',
                content=f'Registered a new growing medium: {new_growing_medium.name}',
            )

            return redirect(new_growing_medium.get_absolute_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

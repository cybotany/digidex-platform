from django.contrib import messages
from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.forms import GrowingMediumForm, GrowingComponentFormSet


class RegisterMediumView(FormView):
    """
    View for registering a new growing medium.
    """
    template_name = 'botany/register_medium.html'
    form_class = GrowingMediumForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["formset"] = GrowingComponentFormSet(self.request.POST, instance=self.object)
        else:
            if not hasattr(self, 'object'):
                self.object = None
            data["formset"] = GrowingComponentFormSet(instance=self.object)
        return data


    def form_valid(self, form):
        """
        If the submitted form is valid, save the info to the database and
        redirect the user to the growing medium detail page.

        Returns:
            Redirects user to the growing medium detail page of the submitted medium.
        """
        self.object = form.save()
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

            Activity.objects.create(
                user=self.request.user,
                activity_status='registered',
                activity_type='growing_medium',
                content=f'Registered a new growing medium: {self.object.name}',
            )

            return redirect('botany:home')
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def get_form_kwargs(self):
        """
        Pass the logged on user object to the GrowingMediumForm.

        Returns:
            kwargs dictionary with the key 'user' assigned to value self.request.user
        """
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

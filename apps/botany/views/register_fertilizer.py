from django.contrib import messages
from django.views.generic import FormView
from django.shortcuts import redirect
from apps.accounts.models import Activity
from apps.botany.forms import GrowingFertilizerForm


class RegisterFertilizerView(FormView):
    template_name = 'register_fertilizer.html'
    form_class = GrowingFertilizerForm

    def form_valid(self, form):
        new_fertilizer = form.save()

        Activity.objects.create(
            user=self.request.user,
            activity_status='registered',
            activity_type='growing_fertilizer',
            content=f'Registered a new fertilizer: {new_fertilizer.name}',
        )

        messages.success(self.request, f'Fertilizer "{new_fertilizer.name}" was successfully added.')
        return redirect('botany:home')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

from django.urls import reverse_lazy
from django.contrib.auth import login
from django.views.generic.edit import FormView
from apps.accounts.forms import SignupForm


class SignupUserView(FormView):
    template_name = 'partials/accounts/signup_user.html'
    form_class = SignupForm
    success_url = reverse_lazy('landing')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super(SignupUserView, self).form_valid(form)

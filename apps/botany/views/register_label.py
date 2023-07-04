from django.views import View
from django.shortcuts import render, redirect
from apps.botany.forms import GrowingLabelForm


class RegisterLabelView(View):
    """
    View for rendering the page used to register plant labels.
    """
    template_name = 'botany/register_label.html'

    def get(self, request):
        form = self.get_form()
        return self.render_form(form)

    def get_form(self):
        return GrowingLabelForm()

    def render_form(self, form):
        context = {'form': form}
        return render(self.request, self.template_name, context)

    def post(self, request):
        form = self.get_form_from_post_request()
        if form.is_valid():
            self.save_label(form)
            return self.redirect_to_home()
        return self.render_form(form)

    def get_form_from_post_request(self):
        return GrowingLabelForm(self.request.POST)

    def save_label(self, form):
        label = form.save(commit=False)
        label.user = self.request.user
        label.save()

    def redirect_to_home(self):
        return redirect('botany:home')

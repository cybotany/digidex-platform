from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import GrowthChamberForm

class DeviceSetupView(LoginRequiredMixin, View):
    template_name = 'device_setup.html'
    
    def get(self, request):
        form = GrowthChamberForm()  # create an empty form
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = GrowthChamberForm(request.POST)  # create a form with the submitted data
        if form.is_valid():
            growth_chamber = form.save(commit=False)
            growth_chamber.user = request.user  # set the current user as the owner
            growth_chamber.save()  # save the growth chamber to the database
            return redirect('dashboard')  # redirect the user to the dashboard page
        else:
            # if the form data is invalid, re-render the form with error messages
            return render(request, self.template_name, {'form': form})
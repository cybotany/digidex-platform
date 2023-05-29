from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import SensorForm, InstrumentForm


class DeviceSetupView(LoginRequiredMixin, View):
    template_name = 'device_setup.html'
    redirect_pattern = reverse('profile')

    def get(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='DeviceAdmins').exists():
            return redirect(self.redirect_pattern)

        sensor_form = SensorForm()
        instrument_form = InstrumentForm()
        context = {
            'sensor_form': sensor_form,
            'instrument_form': instrument_form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = SensorForm(request.POST)
        if form.is_valid():
            growth_chamber = form.save(commit=False)
            growth_chamber.user = request.user
            growth_chamber.save()
            return redirect(self.redirect_pattern)
        else:
            return render(request, self.template_name, {'form': form})

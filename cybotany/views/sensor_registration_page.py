from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from ..forms import SensorForm


class SensorSetupView(LoginRequiredMixin, View):
    template_name = 'sensor_registration.html'

    def get(self, request, *args, **kwargs):
        if not request.user.groups.filter(name='DeviceAdmins').exists():
            return redirect('dashboard')

        sensor_form = SensorForm()
        return render(request, self.template_name, {'sensor_form': sensor_form})

    def post(self, request):
        sensor_form = SensorForm(request.POST)
        if sensor_form.is_valid():
            sensor = sensor_form.save(commit=False)
            sensor.user = request.user
            sensor.save()

            return redirect('dashboard')
        else:
            return render(request, self.template_name, {'sensor_form': sensor_form})

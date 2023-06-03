from django.views import View
from django.shortcuts import render, redirect
from ..forms import PlantRegistrationForm

class RegisterPlant(View):
    template_name = 'botany/plant_form.html'

    def get(self, request):
        form = PlantRegistrationForm(user=request.user)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = PlantRegistrationForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('botany:plant_list')
        context = {'form': form}
        return render(request, self.template_name, context)

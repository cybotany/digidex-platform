from django.views import View
from django.shortcuts import render, redirect
from ..forms import PlantLabelForm


class CreateLabelView(View):
    template_name = 'botany/create_label.html'

    def get(self, request):
        form = PlantLabelForm()
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = PlantLabelForm(request.POST)
        if form.is_valid():
            label = form.save(commit=False)
            label.user = request.user
            label.save()
            return redirect('botany:home')
        context = {'form': form}
        return render(request, self.template_name, context)

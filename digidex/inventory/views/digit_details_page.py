from datetime import datetime
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from digidex.inventory.models import Digit
from digidex.inventory.forms import CreateJournalEntry
from digidex.utils.constants import MAX_DIGIT_THUMBNAIL_DIMMENSIONS


class DigitDetailsView(LoginRequiredMixin, DetailView):
    model = Digit
    template_name = 'main/digit-details-page.html'

    def get_object(self, queryset=None):
        uuid = self.kwargs.get('uuid')
        obj = get_object_or_404(Digit, uuid=uuid)

        if obj.nfc_link.user != self.request.user:
            raise PermissionDenied
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Initialize the form with the current digit and user
        if self.request.method == 'GET':
            context['journal_form'] = CreateJournalEntry()

        journal_entries = self.object.journal_entries.all()
        context['journal_entries'] = journal_entries[:10]

        today = datetime.now().date()

        last_watering_entry = journal_entries.filter(watered=True).order_by('-created_at').first()
        context['last_watering_date'] = last_watering_entry.created_at if last_watering_entry else None
        context['days_since_last_watering'] = (today - last_watering_entry.created_at.date()).days if last_watering_entry else None

        last_fertilizing_entry = journal_entries.filter(fertilized=True).order_by('-created_at').first()
        context['last_fertilizing_date'] = last_fertilizing_entry.created_at if last_fertilizing_entry else None
        context['days_since_last_fertilizing'] = (today - last_fertilizing_entry.created_at.date()).days if last_fertilizing_entry else None
        
        last_cleaning_entry = journal_entries.filter(cleaned=True).order_by('-created_at').first()
        context['last_cleaning_date'] = last_cleaning_entry.created_at if last_cleaning_entry else None
        context['days_since_last_cleaning'] = (today - last_cleaning_entry.created_at.date()).days if last_cleaning_entry else None

        last_image_entry = journal_entries.filter(image__isnull=False).order_by('-created_at').first()
        context['last_image'] = last_image_entry.image if last_image_entry else None

        return context


    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CreateJournalEntry(request.POST, request.FILES)

        if form.is_valid():
            journal_entry = form.save(commit=False)
            journal_entry.digit = self.object
            journal_entry.user = request.user
            journal_entry.save()

            if 'image' in request.FILES:
                image = request.FILES['image']
                img = Image.open(image)
                img.thumbnail(MAX_DIGIT_THUMBNAIL_DIMMENSIONS, Image.ANTIALIAS)

                # Save the processed image to a BytesIO object
                in_memory_image = BytesIO()
                img_format = 'PNG' if img.mode == 'RGBA' else 'JPEG'
                img.save(in_memory_image, format=img_format)
                in_memory_image.seek(0)

                # Create a new Django File from the BytesIO object
                new_image_file = ContentFile(in_memory_image.read())
                new_image_file.name = image.name

                # Update the Digit's thumbnail with the validated image
                #self.object.thumbnail.save(new_image_file.name, new_image_file, save=True)

            return redirect(reverse('inventory:details', kwargs={'uuid': self.object.uuid}))

        context = self.get_context_data()
        context['journal_form'] = form
        return self.render_to_response(context)

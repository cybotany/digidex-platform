from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from nfc.models import NearFieldCommunicationTag
from digitization.forms import DigitizedObjectForm
from inventory.models import UserDigitizedObject, UserDigitizedObjectInventoryPage
from accounts.models import UserProfilePage 

def view_ntag(request, _uuid):
    try:
        ntag = NearFieldCommunicationTag.objects.get(uuid=_uuid)
        if not ntag.digit:
            messages.info(request, "No digit is associated with this NTAG. Please create one. You will be prompted to login if you are not already.")
            return redirect('link-ntag', uuid=_uuid)
        url = ntag.get_dynamic_url()
        return redirect(url)
    except ValidationError as e:
        return HttpResponse(str(e), status=400)

@login_required
def link_ntag(request, _uuid):
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=_uuid)

    try:
        user_profile_page = UserProfilePage.objects.get(user=request.user)
    except UserProfilePage.DoesNotExist:
        messages.error(request, "No profile page found for the current user.")
        return redirect('error_url')

    try:
        inventory_page = UserDigitizedObjectInventoryPage.objects.child_of(user_profile_page).first()
        if not inventory_page:
            messages.error(request, "No inventory page found for the current user.")
            return redirect('error_url')
    except UserDigitizedObjectInventoryPage.DoesNotExist:
        messages.error(request, "Failed to find an inventory page linked to your profile.")
        return redirect('error_url')

    if request.method == 'POST':
        form = DigitizedObjectForm(request.POST)
        if form.is_valid():
            digit = form.save()
            user_digit = UserDigitizedObject.objects.create(
                page=inventory_page,
                digit=digit
            )

            ntag.digit = user_digit
            ntag.save()

            messages.success(request, "Digitized object has been successfully linked.")
            return redirect(ntag.get_dynamic_url())
        else:
            messages.error(request, "There were errors in your form. Please correct them.")
    else:
        form = DigitizedObjectForm()

    return render(request, "digitization/link_digit.html", {'form': form})

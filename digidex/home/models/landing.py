from django.db import models
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth import REDIRECT_FIELD_NAME

from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.models import Page

from home.models import NearFieldCommunicationTag


class LandingPage(Page):
    hero_heading = models.CharField(
        blank=True,
        max_length=255,
    )
    hero_paragraph = models.TextField(
        blank=True,
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('hero_heading'),
                FieldPanel('hero_paragraph'),
            ], heading="Hero Section"
        ),
    ]

    subpage_types = [
        'home.TrainerPage'
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


def route_ntag(request, ntag_uuid):
    ntag = get_object_or_404(NearFieldCommunicationTag, uuid=ntag_uuid)
    try:
        if not ntag.active:
            return HttpResponse("This NFC tag is not active.", status=403)
        if not ntag.page:
            if request.user.is_authenticated:
                return redirect(reverse('home:add_digit', kwargs={'ntag_uuid': ntag_uuid, 'user_slug': request.user.slug}))
            else:
                login_url = reverse('home:login')
                add_digit_url = reverse('home:add_digit', kwargs={'ntag_uuid': ntag_uuid, 'user_slug': request.user.slug})
                return redirect(f'{login_url}?{REDIRECT_FIELD_NAME}={add_digit_url}')
        return redirect(ntag.page.url)
    except ValidationError as e:
        return HttpResponse(str(e), status=400)

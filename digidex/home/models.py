from django.db import models
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.urls import reverse
from django.contrib.auth import REDIRECT_FIELD_NAME

from wagtail.models import Page


class HomePage(Page):


    class Meta:
        verbose_name = "Landing Page"
        verbose_name_plural = "Landing Page"

import logging
logger = logging.getLogger(__name__)

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class AbstractLink(LoginRequiredMixin, View):
    pass

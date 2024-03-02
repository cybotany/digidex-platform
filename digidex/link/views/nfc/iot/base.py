import logging
logger = logging.getLogger(__name__)

from digidex.link.views.nfc import base as nfc_link

class AbstractNfcIotLink(nfc_link.AbstractNfcLink):
    pass

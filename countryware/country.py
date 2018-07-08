import locale
import functools

from django.utils import translation
from django.utils.translation import ugettext as _

from . import defaults as defs
from .utils import TranslationMixin


class Country(TranslationMixin):
    "Singleton translation-aware class for Countries"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.priority = defs.PRIORITY_COUNTRY_CODES


country = Country(prefix="ISO_3166-1.", codes=defs.ALL_COUNTRY_CODES)

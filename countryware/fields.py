from django.contrib.db import models

from . import defaults as defs


class CountryField(models.CharField):
    """ Custom Country Filed """
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 2)
        kwargs.setdefault('choices', defs.COUNTRY_CODES)
        super().__init__(*args, **kwargs)

    def get_internal_type(self):
        return "CharField"

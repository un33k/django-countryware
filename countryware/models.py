
from django.db import models
from django.core.cache import cache
from django.utils.translation import ugettext as _
from django.core.validators import MaxValueValidator, MinValueValidator

from toolware.utils.query import CaseInsensitiveManager, CaseInsensitiveUniqueManager
from .country import get_all_countries_prioritized, get_display
from . import defaults as defs


class Country(models.Model):
    code = models.CharField(
        # Note: admin:skip
        _('Code'),
        max_length=3,
        primary_key=True,
        null=False,
        blank=False,
        # Note: admin:skip
        help_text=_('Country code')
    )

    name = models.CharField(
        # Note: admin:skip
        _('Name'),
        max_length=60,
        null=True,
        blank=True,
        # Note: admin:skip
        help_text=_('Country name (english)'),
    )
  
    # ########## Add new fields above this line #############
    objects = CaseInsensitiveUniqueManager()

    CASE_INSENSITIVE_FIELDS = ['code', 'name']

    @property
    def local_name(self):
        name = get_display(self.code)
        if self.code in name:
            name = self.name
        return name

    def __str__(self):
        return self.local_name

    class Meta:
        # Note: admin:skip
        verbose_name=_('Country')
        # Note: admin:skip
        verbose_name_plural=_('Countries')

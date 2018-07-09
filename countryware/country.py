import locale
import functools

from django.utils import translation
from django.utils.translation import ugettext as _

from . import defaults as defs
from .utils import memorize

_cache_all_countries = {}
_cache_all_countries_sorted = {}
_cache_all_countries_prioritized = {}


def get_display(code):
    # Note: admin:skip
    display = _('ISO_3166-1.' + code)
    return display


def get_countries(codes):
    """ Returns a list of (code, translation) tuples for codes  """
    countries = [(code, _('ISO_3166-1.' + code)) for code in codes]
    return countries


@memorize(_cache_all_countries)
def get_all_countries(codes=defs.ALL_COUNTRY_CODES):
    """ Returns a list of (code, translation) tuples for all country codes  """
    countries = get_countries(codes)
    return countries


@memorize(_cache_all_countries_sorted)
def get_all_countries_sorted(codes=defs.ALL_COUNTRY_CODES):
    """ Returns a list of (code, translation) tuples for all country codes  """
    countries = sorted(
        get_countries(codes),
        key=functools.cmp_to_key(lambda a, b: locale.strcoll(a[1], b[1]))
    )
    return countries


@memorize(_cache_all_countries_prioritized)
def get_all_countries_prioritized(
        priority_codes=defs.PRIORITY_COUNTRY_CODES,
        codes=defs.ALL_COUNTRY_CODES
    ):
    """ Returns a sorted list of (code, translation) tuples for codes  """
    prioritized = []
    if (priority_codes and len(priority_codes) > 0):
        prioritized = get_countries(priority_codes)
    countries = get_all_countries(codes)
    return prioritized + countries
import locale
import functools

from django.utils import translation
from django.utils.translation import ugettext as _

from . import defaults as defs
from .utils import get_cache_key, get_from_cache, set_to_cache


def get_display(code):
    # Note: admin:skip
    display = _('ISO_3166-1.' + code)
    return display


def get_countries(codes):
    """ Returns a list of (code, translation) tuples for codes  """
    countries = [(code, get_display(code)) for code in codes]
    return countries


def get_all_countries(codes=defs.ALL_COUNTRY_CODES):
    """ Returns a list of (code, translation) tuples for all country codes  """
    key = get_cache_key(codes)
    countries = get_from_cache(key)
    if countries:
        return countries
    countries = get_countries(codes)
    set_to_cache(key, countries)
    return countries


def get_all_countries_sorted(codes=defs.ALL_COUNTRY_CODES):
    """ Returns a list of (code, translation) tuples for all country codes  """
    key = get_cache_key(codes, True)
    countries = get_from_cache(key)
    if countries:
        return countries
    countries = sorted(
        get_countries(codes),
        key=functools.cmp_to_key(lambda a, b: locale.strcoll(a[1], b[1]))
    )
    set_to_cache(key, countries)
    return countries


def get_all_countries_prioritized(
        priority_codes=defs.PRIORITY_COUNTRY_CODES,
        codes=defs.ALL_COUNTRY_CODES
    ):
    """ Returns a sorted list of (code, translation) tuples for country codes  """
    codes_subset = list(set(codes) - set(priority_codes))
    key = get_cache_key(priority_codes + codes_subset , True)
    countries = get_from_cache(key)
    if countries:
        return countries
    countries = get_from_cache(key)
    priority_countries = get_all_countries(priority_codes)
    countries = get_all_countries_sorted(codes_subset)
    combined_countries = priority_countries + countries
    set_to_cache(key, combined_countries)
    return combined_countries

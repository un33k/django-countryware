import time

from django.test import TestCase
from django.conf import settings
from django.utils import translation
from django.core.management import call_command

from countryware.country import get_all_countries
from countryware.country import get_all_countries_sorted
from countryware.country import get_all_countries_prioritized
from countryware.country import get_display
from countryware import defaults as defs


class TestCountryCase(TestCase):
    """
    Country Test
    """
    def setUp(self):
        # call_command('compilemessages')
        self.andorra = defs.ALL_COUNTRY_CODES[0]

    def test_xlate_display(self):
        name = get_display('AD')
        self.assertEquals(name, 'Andorra')

    def test_xlate_fa(self):
        translation.activate('fa')
        name = get_display('AD')
        self.assertEquals(name, 'آندورا')

    def test_xlate_fa(self):
        translation.activate('he')
        name = get_display('AD')
        self.assertEquals(name, 'אנדורה')

    def test_xlate_priority(self):
        translation.activate('zh-hans')
        name = get_display('AD')
        self.assertEquals(name, '安道尔')

    def test_xlate_en_unsorted(self):
        translation.activate('en')
        countries = get_all_countries()
        self.assertEquals(countries[0][1], 'Andorra')

    def test_xlate_en_sorted(self):
        translation.activate('en')
        countries = get_all_countries_sorted()
        self.assertEquals(countries[0][1], 'Afghanistan')

    def test_xlate_en_prioritized(self):
        translation.activate('en')
        countries = get_all_countries_prioritized()
        self.assertEquals(countries[0][1], 'Canada')

    def test_xlate_fa_prioritized(self):
        translation.activate('fa')
        countries = get_all_countries_prioritized()
        self.assertEquals(countries[0][1], 'کانادا')
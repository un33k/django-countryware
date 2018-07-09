import time

from django.test import TestCase
from django.conf import settings
from django.utils import translation
from django.core.management import call_command

from countryware.country import country
from countryware import defaults as defs


class TestCountryCase(TestCase):
    """
    Country Test
    """
    def setUp(self):
        # call_command('compilemessages')
        pass
        
    def test_xlate_en(self):
        canada = country.get_display('CA')
        self.assertEquals(canada, 'Canada')

    def test_xlate_fa(self):
        translation.activate('fa')
        canada = country.get_display('CA')
        self.assertEquals(canada, 'کانادا')

    def test_xlate_zh_Hans(self):
        translation.activate('zh_Hans')
        canada = country.get_display('CA')
        self.assertEquals(canada, '加拿大')

    def test_xlate_priority(self):
        translation.activate('en')
        countries = country.get_priority_translations()
        self.assertEquals(countries[0][1], 'Canada')
        # self.assertEquals(countries.count(('CA', 'Canada')), 1)


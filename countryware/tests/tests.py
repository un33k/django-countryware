from django.test import TestCase
from django.conf import settings
from django.utils import translation

from countryware.country import country

class TestCountryCase(TestCase):
    """
    Country Test
    """
    def test_xlate_en(self):
        canada = country.get_display('CA')
        self.assertEquals(canada, 'Canada')

    def test_xlate_fa(self):
        translation.activate('fa')
        canada = country.get_display('CA')
        self.assertEquals(canada, 'کانادا')
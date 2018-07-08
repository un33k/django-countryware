from django.test import TestCase
from django.conf import settings

from countryware.country import country

class TestCountryCase(TestCase):
    """
    Country Test
    """
    def test_xlate(self):
        canada = country.get_display('CA')
        self.assertEquals(canada = 'Canada')
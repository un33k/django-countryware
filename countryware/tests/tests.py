import time

from django.test import TestCase
from django.conf import settings
from django.utils import translation
from django.core.management import call_command

from countryware.country import country


class TestCountryCase(TestCase):
    """
    Country Test
    """
    def setUp(self):
        call_command('compilemessages')

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
from django.apps import apps
from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CountrywareConfig(AppConfig):
    """
    Configuration entry point for the countryware app
    """
    label = name = 'countryware'
    verbose_name = _("countryware app")

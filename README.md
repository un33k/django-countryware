Django Countryware
====================

**A Django application to provides translated country names**

[![status-image]][status-link]
[![version-image]][version-link]
[![coverage-image]][coverage-link]

Overview
====================

**Best attempt** to translate country names while keeping it **DRY**.


How to install
====================

    1. easy_install django-countryware
    2. pip install django-countryware
    3. git clone http://github.com/un33k/django-countryware
        a. cd django-countryware
        b. run python setup.py install
    4. wget https://github.com/un33k/django-countryware/zipball/master
        a. unzip the downloaded file
        b. cd into django-countryware-* directory
        c. run python setup.py install


How to use
====================

   ```python
    # In a models.py
    from countryware.utils.country import country
    from countryware.fields import CountryField

    country = CountryField(
        _("Country"),
        choices=country.get_priority_translations(),

   ```

Advanced users:
====================

   ```python
    # In a settings.py
    # You can overwrite the default list of country codes
    ALL_COUNTRY_CODES = ['US', 'CA', 'MX', 'FR']

    # You can prepend priority countries to the lst
    PRIORITY_COUNTRY_CODES = ['US', 'CA']
   ```

Running the tests
====================

To run the tests against the current environment:

    python manage.py test


License
====================

Released under a ([MIT](LICENSE)) license.


Version
====================
X.Y.Z Version

    `MAJOR` version -- when you make incompatible API changes,
    `MINOR` version -- when you add functionality in a backwards-compatible manner, and
    `PATCH` version -- when you make backwards-compatible bug fixes.

[status-image]: https://secure.travis-ci.org/un33k/django-countryware.png?branch=master
[status-link]: http://travis-ci.org/un33k/django-countryware?branch=master

[version-image]: https://img.shields.io/pypi/v/django-countryware.svg
[version-link]: https://pypi.python.org/pypi/django-countryware

[coverage-image]: https://coveralls.io/repos/un33k/django-countryware/badge.svg
[coverage-link]: https://coveralls.io/r/un33k/django-countryware

[download-image]: https://img.shields.io/pypi/dm/django-countryware.svg
[download-link]: https://pypi.python.org/pypi/django-countryware

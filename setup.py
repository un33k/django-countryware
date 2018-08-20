#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import sys
import codecs
from setuptools import setup, find_packages


name = 'django-countryware'
package = 'countryware'
description = "A Django utility application that provides translated country name services"
url = 'https://github.com/un33k/django-countryware'
author = 'Val Neekman'
author_email = 'info@neekware.com'
license = 'MIT'
install_requires = ['django-toolware>=1.0.5']

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Utilities'

]


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = codecs.open(os.path.join(package, '__init__.py'), encoding='utf-8').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


if sys.argv[-1] == 'build':
    os.system("python setup.py sdist bdist_wheel")

if sys.argv[-1] == 'publish':
    os.system("python setup.py sdist upload")
    args = {'version': get_version(package)}
    print("You probably want to also tag the version now:")
    print("  git tag -a %(version)s -m 'version %(version)s' && git push --tags" % args)
    sys.exit()

EXCLUDE_FROM_PACKAGES = []

setup(
    name=name,
    version=get_version(package),
    url=url,
    license=license,
    description=description,
    long_description=description,
    author=author,
    author_email=author_email,
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    include_package_data=True,
    install_requires=install_requires,
    classifiers=classifiers,
)

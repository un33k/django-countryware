import os
import sys
import codecs
import logging
import json

from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management.base import CommandError
from django.utils.translation import activate

from ...models import Country
from ...country import get_display
from ... import defaults as defs 

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    # Note: admin:skip
    help = 'Load Country data'
    def add_arguments(self, parser):
        parser.add_argument(
            '-f', '--flush',
            dest='flush',
            default=False,
            action='store_true',
            help='delete all existing countries in db'
        )

        parser.add_argument(
            '-o', '--overwrite',
            dest='overwrite',
            action='store_true',
            default=False,
            help='overwrite countries if already found in db'
        )

    def handle(self, *args, **options):
        verbosity = options['verbosity']

        overwrite = options['overwrite']
        flush = options['flush']
        
        if flush:
            self.stdout.write('You are about to delete all countries from db')
            confirm = input('Are you sure? [yes/no]: ')
            if confirm == 'yes':
                Country.objects.all().delete()
                self.stdout.write('countries deleted from db.')

        language = getattr(settings, 'LANGUAGE_CODE', 'en')
        activate(language)
        new_count, update_count = 0, 0
        for code in defs.ALL_COUNTRY_CODES:
            created = False
            defaults = {
                'code': code,
                'name': get_display(code),
            }
            if overwrite:
                instance, created = Country.objects.get_or_create_unique(defaults, ['code'])
            else:
                instance = Country.objects.get_unique_or_none(code=defaults['code'])
                if not instance:
                    instance, created = Country.objects.get_or_create_unique(defaults, ['code'])

            if created:
                new_count += 1
            elif overwrite:
                update_count += 1
        
        self.stdout.write('Created {count} currenies'.format(count=new_count))
        self.stdout.write('Updated {count} currenies'.format(count=update_count))

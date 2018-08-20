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
    path = os.path.abspath(os.path.join(os.path.realpath(__file__), '../../../', 'country.json'))

    def add_arguments(self, parser):
        parser.add_argument(
            '-p',
            '--path',
            dest='path',
            default=self.path,
            help='Path to a json country file.'
        )

        parser.add_argument(
            '--flush',
            dest='flush',
            default=False,
            action='store_true',
            help='delete all existing countries in db'
        )

        parser.add_argument(
            '-l',
            '--load',
            dest='load',
            action='store_true',
            default=False,
            help='Load countries from data file'
        )

        parser.add_argument(
            '-o', '--overwrite',
            dest='overwrite',
            action='store_true',
            default=False,
            help='overwrite countries if already found in db'
        )

    def handle(self, *args, **options):
        self.verbosity = options['verbosity']
        path = options['path']
        overwrite = options['overwrite']
        flush = options['flush']
        load = options['load']
        
        if not (flush or load):
            self.print_help("", subcommand='country')
            return
            
        if flush:
            self.flush()

        if load:
            self.load(path, overwrite)

    def flush(self):
        self.stdout.write('You are about to delete all countries from db')
        confirm = input('Are you sure? [yes/no]: ')
        if confirm == 'yes':
            Country.objects.all().delete()
            self.stdout.write('countries deleted from db.')

    def load(self, path, overwrite):
            
        if not os.path.isfile(path):
            self.stdout.write('No country file found at path')
            self.stdout.write(path)
            self.print_help("", subcommand='country')
            return

        activate(defs.DEFAULT_COUNTRY_LANGUAGE_CODE)

        if self.verbosity > 2:
            self.stdout.write('Preparing country file ...')

        fp = codecs.open(path, encoding='utf-8')
        self.data = json.load(fp)

        new_count, update_count = 0, 0
        for country in self.data:
            created = False
            defaults = {
                'code': country.get('alpha2Code'),
            }
            if defs.DEFAULT_COUNTRY_LANGUAGE_CODE == 'en':
                defaults['name'] = country.get('name')
            else:
                defaults['name'] = get_display(country.get('alpha2Code'))
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
        
        self.stdout.write('Created {count} countries'.format(count=new_count))
        self.stdout.write('Updated {count} countries'.format(count=update_count))

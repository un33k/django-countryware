import locale
import functools

from django.utils import translation
from django.utils.translation import ugettext as _


class TranslationMixin(object):
    """ Translation Mixin """

    _instance = None
    _translated_tuples = {}
    _sorted_translated_tuples = {}
    _sorted_translated_priority_tuples = {}

    def __init__(self, *args, **kwargs):
        self.prefix = kwargs.get('prefix')
        self.codes = kwargs.get('codes')
        self.priority = kwargs.get('priority')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def is_valid_code(self, code):
        valid = code in self.codes
        return valid

    def get_display(self, code):
        # Note: admin:skip
        code = _(self.prefix + code)
        return code

    @property
    def language(self):
        lang = translation.get_language()
        return lang

    def _get_translations(self, codes):
        translated = self._translated_tuples.get(self.language)
        if translated is None:
            translated = [(code, self.get_display(code)) for code in codes]
            self._translated_tuples[self.language] = translated
        return translated

    def _get_translations_sorted(self, codes):
        sorted_translated = self._sorted_translated_tuples.get(self.language)
        if sorted_translated is None:
            sorted_translated = sorted(
                self._get_translations(codes),
                key=functools.cmp_to_key(lambda a, b: locale.strcoll(a[1], b[1]))
            )
            self._sorted_translated_tuples[self.language] = sorted_translated
        return sorted_translated

    def _get_priority_translations(self, priority, codes):
        translated = self._sorted_translated_priority_tuples.get(self.language)
        if translated is None:
            priority = self._get_translations(priority)
            _codes = [code for code in codes if code not in priority]
            sorted = self._get_translations_sorted(_codes)
            self._translated_tuples[self.language] = priority + sorted
        return self._translated_tuples[self.language]

    def get_translations(self, codes):
        """ Returns a list of (code, translation) tuples for codes  """
        codes = codes or self.codes
        return self._get_priority_translations(priority, codes)

    def get_translations_sorted(self, codes):
        """ Returns a sorted list of (code, translation) tuples for codes  """
        codes = codes or self.codes
        return self._get_priority_translations(priority, codes)

    def get_priority_translations(self, priority, codes):
        """ Returns a list of (code, translation) tuples for priority, codes  """
        priority = priority or self.priority
        codes = codes or self.codes
        return self._get_priority_translations(priority, codes)

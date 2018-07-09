import locale
import functools

from django.utils import translation
from django.utils.translation import ugettext as _


def memorize(cache):
    def decorator(function):
        def wrapper(*args, **kwargs):
            lang = translation.get_language()
            result = cache.get(lang)
            if result is None:
                result = function(*args, **kwargs)
                cache[lang] = result
            return result
        return wrapper
    return decorator

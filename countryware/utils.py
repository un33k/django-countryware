from django.core.cache import cache
from django.utils import translation
from django.utils.translation import ugettext as _

_cache_countries = {}
_cache_backend_enabled = None


def check_cache():    
    """ Check if a cache backend is available """
    global _cache_backend_enabled
    if _cache_backend_enabled is None:
        value = 100
        key = 'testing-if-cache-is-enabled'
        try:
            cache.set(key, value)
            if cache.get(key) == value:
                _cache_backend_enabled = True
        except Exception:
            _cache_backend_enabled = False


def get_from_cache(key):
    """ get value for key from cache """
    check_cache()
    if _cache_backend_enabled:
        return cache.get(key)
    return _cache_countries.get(key)


def set_to_cache(key, value):
    """ set value for key to cache """
    check_cache()
    if _cache_backend_enabled:
        cache.set(key, value)
    else:
        _cache_countries[key] = value


def get_cache_key(codes, sorted=False):
    """ get cache key for operation """
    unique = hash(tuple(codes))
    lang = translation.get_language()
    key = '{}-{}-{}'.format(unique, lang, sorted)
    return key

from django.core.cache import cache
from django.utils import translation
from django.utils.translation import ugettext as _

_cache_enabled = None


def check_cache():    
    """ Check if a cache backend is available """
    global _cache_enabled
    if _cache_enabled is None:
        value = 100
        key = 'testing-if-cache-is-enabled'
        try:
            cache.set(key, value)
            if cache.get(key) == value:
                _cache_enabled = True
        except Exception:
            _cache_enabled = False


def get_from_cache(backend, key):
    if _cache_enabled is True:
        return cache.get(key)
    return backend.get(key)


def set_to_cache(backend, key, value):
    if _cache_enabled is True:
        cache.set(key, value)
    else:
        backend[key] = value


def memorize(cache_storage):
    def decorator(function):
        def wrapper(*args, **kwargs):
            check_cache()
            lang = translation.get_language()
            result = get_from_cache(cache_storage, lang)
            if result is None:
                result = function(*args, **kwargs)
                set_to_cache(cache_storage, lang, result)
            return result
        return wrapper
    return decorator

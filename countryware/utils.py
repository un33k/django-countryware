import inspect

from django.core.cache import cache
from django.utils import translation
from django.utils.translation import ugettext as _

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


def get_from_cache(backend, key):
    """ get value for key from cache """
    if _cache_backend_enabled is True:
        return cache.get(key)
    return backend.get(key)


def set_to_cache(backend, key, value):
    """ set value for key to cache """
    if _cache_backend_enabled is True:
        cache.set(key, value)
    else:
        backend[key] = value


def get_cache_key(backend):
    """ get cache key for operation """
    lang = translation.get_language()
    key = '{}-{}'.format(id(backend), lang)
    return key


def memorize(cache_storage):
    """ decorator to cache operation """
    def decorator(function):
        def wrapper(*args, **kwargs):
            check_cache()
            key = get_cache_key(cache_storage)
            result = get_from_cache(cache_storage, key)
            if result is None:
                result = function(*args, **kwargs)
                set_to_cache(cache_storage, key, result)
            return result
        return wrapper
    return decorator

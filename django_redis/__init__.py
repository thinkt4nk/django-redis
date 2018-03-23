# -*- coding: utf-8 -*-

__version__ = '4.8.0.ambition'


def get_redis_connection(alias='default', write=True):
    """
    Helper used for obtaining a raw redis client.
    """

    from django.core.cache import caches

    cache = caches[alias]

    if not hasattr(cache, "client"):
        raise NotImplementedError("This backend does not support this feature")

    if not hasattr(cache.client, "get_client"):
        raise NotImplementedError("This backend does not support this feature")

    return cache.client.get_client(write)

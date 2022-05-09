import logging

import redis

import settings

LOGGER = logging.getLogger('sLogger')


class Cache:

    def __init__(self) -> None:
        LOGGER.debug('connecting to Redis...')
        self.__redis = redis.from_url(url=settings.REDIS_HOST)
        LOGGER.debug('sucesfully connected to Redis.')

    def get(self, key: str):
        return self.__redis.get(key)

    def set(self, key: str, data, ttl: int) -> None:
        self.__redis.set(
            key,
            data,
            ex=ttl
        )

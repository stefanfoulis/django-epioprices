#-*- coding: utf-8 -*-
import datetime


MONTH = datetime.timedelta(days=30)
QUARTER = datetime.timedelta(days=365/4)
YEAR = datetime.timedelta(days=365)


class BaseInstance(object):
    free_memory_limit = 0.0  # in MB
    hourly_rate = 0.03  # in $
    hourly_rate_memory = 128.0  # in MB
    
    def __init__(self, memory_usage=None):
        self.memory_usage = memory_usage or self.free_memory_limit

    def price(self, duration=None):
        duration = duration or MONTH

        if self.memory_usage <= self.free_memory_limit:
            return 0.0
        hourly_price = (self.memory_usage / self.hourly_rate_memory) * self.hourly_rate
        return hourly_price * (duration.total_seconds()/3600)


class WebInstance(BaseInstance):
    code = 'web'
    name = 'Web'


class RedisInstance(BaseInstance):
    code = 'redis'
    name = 'Redis'
    free_memory_limit = 16.0  # in MB


class CeleryInstance(BaseInstance):
    code = 'celery'
    name = 'Celery'


class Bandwidth(object):
    free = 5.0  # in GB
    rate = 0.15  # in $ per GB

    def __init__(self, usage):
        self.usage = usage

    def price(self, duration=None):
        duration = duration or MONTH
        if self.free >= self.usage:
            payable = 0.0
        else:
            payable = self.usage - self.free
        return payable * self.rate * (duration.total_seconds()/MONTH.total_seconds())


class Storage(object):
    free = 2.0  # in GB/Months
    rate = 0.5  # in $ per GB/Month

    def __init__(self, usage):
        self.usage = usage

    def price(self, duration=None):
        duration = duration or MONTH
        if self.free >= self.usage:
            payable = 0.0
        else:
            payable = self.usage - self.free
        return payable * self.rate * (duration.total_seconds()/MONTH.total_seconds())
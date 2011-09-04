#-*- coding: utf-8 -*-
from django.db import models
from .prices import WebInstance, CeleryInstance, RedisInstance, Bandwidth, Storage, MONTH, QUARTER, YEAR


INSTANCE_TYPES = (WebInstance, CeleryInstance, RedisInstance)
INSTANCE_TYPES_LOOKUP = dict([(i.code, i) for i in INSTANCE_TYPES])
INSTANCE_TYPE_CHOICES = [(i.code, i.name) for i in INSTANCE_TYPES]


class Deployment(models.Model):
    name = models.CharField(max_length=255, default='', blank=True)
    description = models.TextField(default='', blank=True)
    storage_usage = models.FloatField(default=2.0, help_text='storage space used in GB (contains db, project and files)')
    bandwidth_usage = models.FloatField(default=5.0, help_text='monthly bandwidth usage in GB')

    def bandwidth_cost(self, duration=MONTH):
        if self.bandwidth_usage:
            return Bandwidth(usage=self.bandwidth_usage).price(duration)
        return 0.0

    def storage_cost(self, duration=MONTH):
        if self.storage_usage:
            return Storage(usage=self.storage_usage).price(duration)
        return 0.0

    def instance_cost(self, duration=MONTH):
        return sum([i.total_cost(duration) for i in self.instance_set.all()])

    def first_instance_rebate(self, duration=MONTH):
        """
        we assume the first instance rebate applies to the first web instance only.
        """
        for instance in self.instance_set.filter(instance_type='web'):
            return (-1) * (instance.cost(duration=duration, amount=1) / 2.0)
        return -0.0

    def total_cost(self, duration=MONTH):
        return sum([self.bandwidth_cost(duration), self.storage_cost(duration),
                    self.instance_cost(duration)])

class Instance(models.Model):
    deployment = models.ForeignKey(Deployment)
    amount = models.IntegerField(default=1)
    instance_type = models.CharField(choices=INSTANCE_TYPE_CHOICES, max_length=128)
    memory_usage = models.FloatField(default=128, help_text='memory usage in MB')

    def cost(self, duration=MONTH, amount=None):
        amount = amount or self.amount
        if self.calculator:
            return self.calculator(memory_usage=self.memory_usage).price(duration=duration) * amount
        else:
            return 0.0

    def total_cost(self, duration=MONTH):
        return self.cost(duration) * self.amount

    @property
    def calculator(self):
        if self.instance_type:
            return INSTANCE_TYPES_LOOKUP[self.instance_type]
        else:
            return None

#-*- coding: utf-8 -*-
from django.contrib import admin
from .models import Deployment, Instance


class InstanceInline(admin.TabularInline):
    model = Instance
    readonly_fields = ('cost', 'total_cost',)


class DeploymentAdmin(admin.ModelAdmin):
    readonly_fields = ('bandwidth_cost', 'storage_cost', 'instance_cost', 'first_instance_rebate', 'total_cost')
    list_display = ('name', 'storage_usage', 'bandwidth_usage', ) + readonly_fields
    inlines = (InstanceInline,)
    fieldsets = (
        (None, {'fields': ('name', ('storage_usage', 'bandwidth_usage'))}),
        (None, {'fields': ('total_cost',
                           ('bandwidth_cost', 'storage_cost', 'instance_cost',),
                           'first_instance_rebate',
            )}),
        ('description', {'fields': ('description',), 'classes': ('collapse',)}),
    )

    def total_cost(self, obj):
        return u'<strong style="font-size: 24px;">$ %s</strong>' % obj.total_cost()
    total_cost.allow_tags = True

    def bandwidth_cost(self, obj):
        return u'<strong style="font-size: 18px;">$ %s</strong>' % obj.bandwidth_cost()
    bandwidth_cost.allow_tags = True

    def storage_cost(self, obj):
        return u'<strong style="font-size: 18px;">$ %s</strong>' % obj.storage_cost()
    storage_cost.allow_tags = True

    def instance_cost(self, obj):
        return u'<strong style="font-size: 18px;">$ %s</strong>' % obj.instance_cost()
    instance_cost.allow_tags = True

    def first_instance_rebate(self, obj):
        return u'<strong style="font-size: 18px;">$ %s</strong>' % obj.first_instance_rebate    ()
    first_instance_rebate.allow_tags = True


admin.site.register(Deployment, DeploymentAdmin)
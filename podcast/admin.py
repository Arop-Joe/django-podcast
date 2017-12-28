from django.contrib import admin
from . import models


class ChannelAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'link', 'description')
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': (
                'language',
                'copyright',
                'managing_editor',
                'web_master',
                'pub_date',
                'last_build_date',
                'ttl',
                'generator'
            )
        }),
        ('iTunes', {
            'classes': ('collapse',),
            'fields': (
                'subtitle', 'summary', 'block', 'redirect', 'keywords', 'itunes'
            )
        })
    )

admin.site.register(models.Channel, ChannelAdmin)
admin.site.register(models.Item)
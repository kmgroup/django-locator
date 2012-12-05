from django.contrib import admin

from .models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'state', 'latitude', 'longitude')
    list_filter = ('city', 'state')
    fieldsets = (
        (None, {
            'fields': ('name', ('latitude', 'longitude'))
        }),
        ('Address', {
            'fields': ('street', ('city', 'state', 'postal'))
        }),
        ('Optional', {
            'fields': ('phone', 'website', 'hours')
        }),
    )


admin.site.register(Location, LocationAdmin)

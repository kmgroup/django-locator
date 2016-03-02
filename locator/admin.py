from django.contrib import admin

from .models import Location

def make_active(modeladmin, request, queryset):
    queryset.update(active=True)

make_active.short_description = "1) Mark selected items as Active"

def make_active_not(modeladmin, request, queryset):
    queryset.update(active=False)

make_active_not.short_description = "2) Mark selected items as Inactive"


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'active', 'city', 'state', 'latitude', 'longitude')
    list_filter = ('city', 'state')
    fieldsets = (
        (None, {
            'fields': ('name', 'active', ('latitude', 'longitude'))
        }),
        ('Address', {
            'fields': ('street', ('city', 'state', 'postal'))
        }),
        ('Optional', {
            'fields': ('phone', 'website', 'hours')
        }),
    )
    actions = [make_active, make_active_not]
    ordering = ('-active', 'name')


admin.site.register(Location, LocationAdmin)

from django.contrib import admin

from applications.maps.models import Map


@admin.register(Map)
class MapsAdmin(admin.ModelAdmin):
    list_display = ['name', 'map_type', 'coordinates', ]
    list_filter = ['map_type', ]
    search_fields = ['name', ]

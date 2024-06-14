from adminsortable2.admin import SortableAdminMixin

from django.contrib import admin

from applications.tariffs.models import TvTariff, InternetTariff


@admin.register(TvTariff)
class SmartTvTariffAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'channels_count', 'price']
    list_filter = ['city', 'tech_type']
    filter_horizontal = ['city']


@admin.register(InternetTariff)
class SmartTvTariffAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'speed', 'price', 'extra_neo_tv', 'extra_smart_tv']
    list_filter = ['city', 'tech_type']
    filter_horizontal = ['city']

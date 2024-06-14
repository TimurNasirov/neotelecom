from django.contrib import admin

from applications.promotions.models import Promotion


@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date', 'is_visible']
    list_filter = ['city', 'is_visible']
    filter_horizontal = ['city']

from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin

from applications.handbook.models import HandBook


@admin.register(HandBook)
class HandBookAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['category', 'title']
    list_filter = ['category']

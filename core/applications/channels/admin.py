from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.utils.safestring import mark_safe

from applications.channels.models import Channel


@admin.register(Channel)
class BannerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'image_preview_50']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']

    def image_preview_50(self, obj):
        img = f'<img width=50 src={obj.image.url} style="margin: auto; display: block;"/>'
        return mark_safe(img)
    image_preview_50.short_description = 'Логотип'

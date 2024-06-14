from adminsortable2.admin import SortableAdminMixin
from django.contrib import admin
from django.templatetags.static import static
from django.utils.safestring import mark_safe

from applications.banners.models import Banner, BannerStatistics


class BannerStatisticsInline(admin.TabularInline):
    model = BannerStatistics
    exclude = ['is_delete']
    can_delete = False
    readonly_fields = ['count_view', 'count_click']


@admin.register(Banner)
class BannerAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = [
        'name', 'is_active', 'end_date',
        'image_preview_50', 'statistics_field', 'create_update_date',
    ]
    search_fields = ['name']
    list_filter = ['end_date']
    inlines = [BannerStatisticsInline]
    readonly_fields = ['image_preview_50', 'image_preview_150']

    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['name', 'is_visible', 'url', 'image', 'image_preview_150']
        }),
        ('Даты отображения', {
            'description': (
                'Блок с датами включения/отключения баннера. '
                'Так же можно отключить баннер руками через "Отображать на сайте"'
            ),
            'fields': ['start_date', 'end_date']
        }),
    ]

    def is_active(self, obj):
        url = static('admin/img/icon-{}.svg'.format('yes' if obj.is_active else 'no'))
        tmp = f'<img src="{url}" alt="{obj.is_active}">'
        return mark_safe(tmp)

    is_active.short_description = 'Активный'

    def start_end_date(self, obj):
        data = [
            '{}: {}'.format(self._get_verbose_name_field(obj, 'start_date'), obj.start_date),
            '{}: {}'.format(self._get_verbose_name_field(obj, 'end_date'), obj.end_date),
        ]
        return mark_safe('<br>'.join(data))

    start_end_date.short_description = 'Запуск/Завершение'

    def statistics_field(self, obj):
        data = [
            '{}: {}'.format(self._get_verbose_name_field(obj.statistics, 'count_view'), obj.statistics.count_view),
            '{}: {}'.format(self._get_verbose_name_field(obj.statistics, 'count_click'), obj.statistics.count_click),
        ]
        return mark_safe('<br>'.join(data))

    statistics_field.short_description = 'Статистика'

    def create_update_date(self, obj):
        date_format = '%m-%d-%Y %H:%M:%S'
        data = [
            '{}: {}'.format(self._get_verbose_name_field(obj, 'created_at'), obj.created_at.strftime(date_format)),
            '{}: {}'.format(self._get_verbose_name_field(obj, 'updated_at'), obj.updated_at.strftime(date_format)),
        ]
        return mark_safe('<br>'.join(data))

    create_update_date.short_description = 'Создано/Изменение'

    def image_preview_50(self, obj):
        tmp = f'<img width=50 src={obj.image.url} />'
        return mark_safe(tmp)

    image_preview_50.short_description = 'Предпросмотр изображения'

    def image_preview_150(self, obj):
        tmp = f'<img width=150 src={obj.image.url} />'
        return mark_safe(tmp)

    image_preview_150.short_description = 'Предпросмотр изображения'

    @staticmethod
    def _get_verbose_name_field(obj, field_name):
        for field in obj._meta.concrete_fields:
            if field.name == field_name:
                return field.verbose_name
        return ''

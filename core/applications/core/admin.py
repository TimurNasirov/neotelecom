from django.contrib import admin

from applications.core.models import City, JoinUs, CallMe, Vacancy, NeoTvFiles

admin.AdminSite.site_header = 'NeoTelecom'
admin.AdminSite.index_title = 'NeoTelecom'


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active']
    prepopulated_fields = {"slug": ("title",)}

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


@admin.register(JoinUs)
class JoinUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address', 'form_type', 'status', 'ownership', ]
    list_filter = ['status', 'form_type', 'ownership', ]
    search_fields = ['name', 'phone', ]
    readonly_fields = ['name', 'phone', 'address', 'ownership',  'form_type', ]
    actions = []

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(CallMe)
class CallMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'status', ]
    list_filter = ['status', ]
    search_fields = ['name', 'phone', ]
    readonly_fields = ['name', 'phone', ]
    actions = []

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    pass


@admin.register(NeoTvFiles)
class NeoTvFilesAdmin(admin.ModelAdmin):
    pass

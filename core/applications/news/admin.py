from django.contrib import admin

from applications.news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'news_type', 'created_at']
    list_filter = ['news_type']

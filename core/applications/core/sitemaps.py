from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return [
            'main_page',
            'promotions',
            'news',
            'join_us',
            'tariffs',
            'handbook',
            'channels',
        ]

    def location(self, item):
        return reverse(item)

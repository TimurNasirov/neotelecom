from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include

from applications.channels.views import channels_view
from applications.core.sitemaps import StaticViewSitemap
from applications.core.views import main_page_view, join_us_view, city_switcher, custom_handler404, custom_pages_view, \
    create_callback, vacancies_list, vacancies_detail, neo_tv_view, add_join_us
from applications.handbook.views import handbook_view, handbook_category_view
from applications.maps.views import get_map_coordinates, map_view
from applications.news.views import news_list_view, news_details_view
from applications.promotions.views import promotion_detail_view, promotion_list_view
from applications.tariffs.views import tariffs_view

handler404 = custom_handler404

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    # =================== BASE ===========================
    path('admin/', admin.site.urls),
    path('', main_page_view, name='main_page'),

    # =================== CITY ===========================
    path('city/<slug:city_slug>', city_switcher, name='city_switcher'),

    # =================== PROMO ==========================
    path('promotions/', promotion_list_view, name='promotions'),
    path('promotions/<int:promotion_id>/', promotion_detail_view, name='promotion_details'),

    # =================== NEWS ===========================
    path('news/', news_list_view, name='news'),
    path('news/<int:news_id>/', news_details_view, name='news_details'),

    # =================== VACANCIES ======================
    path('vacancies/', vacancies_list, name='vacancies'),
    path('vacancies/<int:vacancies_id>/', vacancies_detail, name='vacancy_details'),

    # =================== JOIN US ========================
    path('join_us/', join_us_view, name='join_us'),

    # =================== MAP ============================
    path('map/<str:map_type>/', map_view, name='map'),

    # =================== TARIFFS ========================
    path('tariffs/', tariffs_view, name='tariffs'),

    # =================== HANDBOOK =======================
    path('handbook/<slug:category>/', handbook_category_view, name='handbook_category'),
    path('handbook/', handbook_view, name='handbook'),

    # =================== CHANNELS =======================
    path('channels/', channels_view, name='channels'),

    # =================== API ============================
    path('api/v1/map/<str:map_type>/', get_map_coordinates),
    path('api/v1/callback_form/', create_callback),
    path('api/v1/join_us', add_join_us),

    # =================== CUSTOM PAGES ===================
    path('neotv/', neo_tv_view),
    path('<str:page_name>/', custom_pages_view),

    # =================== SYSTEM =========================
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

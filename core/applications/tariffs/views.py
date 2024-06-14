from django.shortcuts import render

from applications.core.models import City
from applications.tariffs.models import InternetTariff, TvTariff


def tariffs_view(request):
    city_slug = request.COOKIES.get('city') or 'bishkek'
    city = City.objects.filter(slug=city_slug).last()

    internet_gpon = InternetTariff.objects.filter(tech_type='gpon', city=city).all()
    internet_4g = InternetTariff.objects.filter(tech_type='4g', city=city).all()

    smart_tv = TvTariff.objects.filter(tech_type='smart_tv', city=city).all()
    neo_tv = TvTariff.objects.filter(tech_type='neo_tv', city=city).all()

    return render(request, 'tariffs.html', context={
        'gpon': internet_gpon,
        '4g': internet_4g,
        'smart_tv': smart_tv.filter(extra_package=False),
        'neo_tv': neo_tv.filter(extra_package=False),
        'ext_smart_tv': smart_tv.filter(extra_package=True),
        'ext_neo_tv': neo_tv.filter(extra_package=True),
    })
